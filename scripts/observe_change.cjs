// Run: node scripts/observe_change.cjs <path-to-coredns.exe> [output.json]
// The downloaded CoreDNS binary must be checked against its official checksum.
const fs = require('node:fs');
const path = require('node:path');
const {spawn, execFileSync} = require('node:child_process');
const {Resolver} = require('node:dns').promises;
const assert = require('node:assert/strict');

const binary = path.resolve(process.argv[2] || '');
if (!process.argv[2] || !fs.existsSync(binary)) throw new Error('Supply a verified CoreDNS binary');
const output = path.resolve(process.argv[3] || 'references/observations/change-2026-11-20.json');
const work = path.resolve('.review', `change-lab-${Date.now()}`);
fs.mkdirSync(work, {recursive:true});
const config = `lab.test:15354 {
    bind 127.0.0.1
    file db.lab.test lab.test {
        reload 1s
    }
    errors
}
lab.test:15353 {
    bind 127.0.0.1
    cache 300
    forward . 127.0.0.1:15354
    errors
}
`;
const zone = (serial, address, ttl, added) => `$ORIGIN lab.test.
$TTL 20
@ 20 IN SOA ns.lab.test. hostmaster.lab.test. ${serial} 60 60 600 20
@ IN NS ns.lab.test.
ns IN A 127.0.0.1
app ${ttl} IN A ${address}
${added ? 'new 5 IN A 192.0.2.3\n' : ''}`;
const beforeZone=zone(1,'192.0.2.1',20,false);
const afterZone=zone(2,'192.0.2.2',5,true);
fs.writeFileSync(path.join(work,'Corefile'),config);
fs.writeFileSync(path.join(work,'db.lab.test'),beforeZone);
const authority = new Resolver({timeout:500,tries:1});authority.setServers(['127.0.0.1:15354']);
const cache = new Resolver({timeout:500,tries:1});cache.setServers(['127.0.0.1:15353']);
let logs='';
const child=spawn(binary,['-conf','Corefile'],{cwd:work,windowsHide:true,stdio:['ignore','pipe','pipe']});
child.stdout.on('data',x=>logs+=x);child.stderr.on('data',x=>logs+=x);
let spawnError;child.on('error',e=>spawnError=e);
const delay=ms=>new Promise(resolve=>setTimeout(resolve,ms));
const started=Date.now();
const events=[];
async function sample(label, resolver, name) {
  const event={label,name,at_utc:new Date().toISOString(),elapsed_ms:Date.now()-started};
  try {event.answers=await resolver.resolve4(name,{ttl:true});event.status='answered';}
  catch(e) {event.status=e.code;}
  events.push(event);return event;
}
(async()=>{
  try {
    let ready=false;
    for(let i=0;i<30;i++) {
      if(spawnError) throw spawnError;
      if(child.exitCode!==null) throw new Error(logs);
      try {await authority.resolve4('app.lab.test');ready=true;break;} catch {await delay(100);}
    }
    assert.ok(ready,'Authority did not start');
    const first=await sample('cache-before-change',cache,'app.lab.test');
    assert.equal(first.answers[0].address,'192.0.2.1');
    const negative=await sample('negative-before-addition',cache,'new.lab.test');
    assert.equal(negative.status,'ENOTFOUND');
    fs.writeFileSync(path.join(work,'db.lab.test'),afterZone);
    events.push({label:'zone-file-changed',at_utc:new Date().toISOString(),elapsed_ms:Date.now()-started,serial:2});
    let updated=false;
    for(let i=0;i<30;i++) {
      const answers=await authority.resolve4('app.lab.test',{ttl:true});
      if(answers[0].address==='192.0.2.2'){updated=true;break;}
      await delay(100);
    }
    assert.ok(updated,'Authority did not reload changed serial');
    await sample('authority-after-change',authority,'app.lab.test');
    await sample('cache-after-change',cache,'app.lab.test');
    await sample('authority-after-addition',authority,'new.lab.test');
    await sample('negative-cache-after-addition',cache,'new.lab.test');
    await delay(Math.max(0, first.elapsed_ms+22000-(Date.now()-started)));
    const fresh=await sample('cache-after-old-expiry',cache,'app.lab.test');
    const added=await sample('cache-after-negative-expiry',cache,'new.lab.test');
    assert.equal(fresh.answers[0].address,'192.0.2.2');
    assert.equal(added.answers[0].address,'192.0.2.3');
    const result={software:execFileSync(binary,['-version'],{windowsHide:true,encoding:'utf8'}).trim(),node:process.version,vantage:'Windows loopback only; no external DNS forwarding',authority:'127.0.0.1:15354',cache:'127.0.0.1:15353',config,before_zone:beforeZone,after_zone:afterZone,events};
    fs.mkdirSync(path.dirname(output),{recursive:true});fs.writeFileSync(output,JSON.stringify(result,null,2)+'\n');
    console.log(JSON.stringify(result,null,2));
  } finally {child.kill();}
})().catch(e=>{console.error(e,logs);process.exitCode=1;});
