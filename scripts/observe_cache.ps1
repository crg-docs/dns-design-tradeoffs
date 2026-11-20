param(
    [string]$Name = 'example.com',
    [string]$Server = '1.1.1.1',
    [string]$OutputPath = 'references/observations/cache-2026-11-20.json'
)

$ErrorActionPreference = 'Stop'
$samples = @()
for ($sample = 1; $sample -le 3; $sample++) {
    $started = [DateTimeOffset]::UtcNow
    $timer = [Diagnostics.Stopwatch]::StartNew()
    $answer = Resolve-DnsName -Name $Name -Type A -Server $Server -DnsOnly -NoHostsFile
    $timer.Stop()
    $samples += [ordered]@{
        sample = $sample
        started_utc = $started.ToString('o')
        started_jst = $started.ToOffset([TimeSpan]::FromHours(9)).ToString('o')
        elapsed_ms = [Math]::Round($timer.Elapsed.TotalMilliseconds, 3)
        answers = @($answer | Where-Object Type -eq 'A' | ForEach-Object {
            [ordered]@{ name = $_.Name; type = 'A'; ttl_seconds = $_.TTL; address = $_.IPAddress }
        })
    }
    if ($sample -lt 3) { Start-Sleep -Seconds 2 }
}
$record = [ordered]@{
    purpose = 'Observe returned TTLs, not benchmark resolver performance'
    vantage = 'Author Windows workstation; geographic location and resolver backend not determined'
    powershell_version = $PSVersionTable.PSVersion.ToString()
    command = "Resolve-DnsName -Name $Name -Type A -Server $Server -DnsOnly -NoHostsFile"
    query_count = 3
    interval_after_response_seconds = 2
    cache_flush_performed = $false
    samples = $samples
}
$directory = Split-Path -Parent $OutputPath
if ($directory) { New-Item -ItemType Directory -Force $directory | Out-Null }
$observationJson = (($record | ConvertTo-Json -Depth 8) -replace '\r\n', "`n") + "`n"
$observationJson | Set-Content -Encoding utf8 -NoNewline $OutputPath
$record | ConvertTo-Json -Depth 8
