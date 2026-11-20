param([string]$OutputPath = '.review/privacy-rerun.json')
$ErrorActionPreference = 'Stop'
$name = 'example.com'
$plainAt = [DateTimeOffset]::UtcNow.ToString('o')
$plain = @(Resolve-DnsName -Name $name -Type A -Server 1.1.1.1 -DnsOnly |
    Where-Object Type -eq A | Select-Object Name, Type, TTL, IPAddress)
$uri = 'https://cloudflare-dns.com/dns-query?name=example.com&type=A'
$httpsAt = [DateTimeOffset]::UtcNow.ToString('o')
$response = Invoke-WebRequest -Uri $uri -Headers @{Accept='application/dns-json'}
$body = if ($response.Content -is [byte[]]) { [Text.Encoding]::UTF8.GetString($response.Content) } else { [string]$response.Content }
$result = [ordered]@{
    vantage = 'Windows; one client; no OS resolver settings changed'
    query_name = $name
    plain = @{at_utc=$plainAt; server='1.1.1.1'; command='Resolve-DnsName -Name example.com -Type A -Server 1.1.1.1 -DnsOnly'; answers=$plain}
    https_json = @{at_utc=$httpsAt; uri=$uri; accept='application/dns-json'; status_code=[int]$response.StatusCode; content_type=[string]($response.Headers['Content-Type'] -join ','); response=($body | ConvertFrom-Json)}
    limits = 'Provider JSON API, not RFC 8484 wire-format observation. No packet capture, upstream tracing, location comparison, or logging-policy verification.'
}
$directory = Split-Path -Parent $OutputPath
if ($directory) { New-Item -ItemType Directory -Path $directory -Force | Out-Null }
$json = ($result | ConvertTo-Json -Depth 15) -replace "`r`n", "`n"
Set-Content -LiteralPath $OutputPath -Value ($json + "`n") -NoNewline -Encoding utf8
Write-Output $json
