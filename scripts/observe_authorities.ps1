param(
    [string]$Name = 'iana.org',
    [string]$DiscoveryServer = '1.1.1.1',
    [string]$OutputPath = 'references/observations/authorities-2026-11-20.json'
)
$ErrorActionPreference = 'Stop'
$started = [DateTimeOffset]::UtcNow
$names = @(Resolve-DnsName -Name $Name -Type NS -Server $DiscoveryServer -DnsOnly -NoHostsFile |
    Where-Object Type -eq 'NS' | Select-Object -ExpandProperty NameHost | Sort-Object -Unique)
$results = @()
foreach ($server in ($names | Select-Object -First 2)) {
    $sampleTime = [DateTimeOffset]::UtcNow
    try {
        $answer = @(Resolve-DnsName -Name $Name -Type SOA -Server $server -DnsOnly -NoHostsFile -NoRecursion |
            Where-Object Type -eq 'SOA' | Select-Object Name, PrimaryServer, SerialNumber, TimeToZoneRefresh, TimeToZoneFailureRetry, TimeToExpiration)
        $results += [ordered]@{ server = $server; started_jst = $sampleTime.ToOffset([TimeSpan]::FromHours(9)).ToString('o'); status = 'answered'; soa = $answer }
    } catch {
        $results += [ordered]@{ server = $server; started_jst = $sampleTime.ToOffset([TimeSpan]::FromHours(9)).ToString('o'); status = 'failed'; error = $_.Exception.Message }
    }
}
$record = [ordered]@{
    purpose = 'Observe responses from two named authoritative endpoints; not a fault injection test'
    vantage = 'Author Windows workstation; geographic location and server physical placement not determined'
    started_utc = $started.ToString('o')
    name = $Name
    discovery_server = $DiscoveryServer
    names = $names
    discovery_command = "Resolve-DnsName -Name $Name -Type NS -Server $DiscoveryServer -DnsOnly -NoHostsFile"
    query_template = "Resolve-DnsName -Name $Name -Type SOA -Server <server> -DnsOnly -NoHostsFile -NoRecursion"
    powershell_version = $PSVersionTable.PSVersion.ToString()
    results = $results
}
New-Item -ItemType Directory -Force (Split-Path -Parent $OutputPath) | Out-Null
$observationJson = (($record | ConvertTo-Json -Depth 8) -replace '\r\n', "`n") + "`n"
$observationJson | Set-Content -Encoding utf8 -NoNewline $OutputPath
$observationJson
