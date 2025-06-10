# bootstrap_env.ps1
$env:PYTHONPATH = Join-Path $PSScriptRoot "..\src"
Write-Host "PYTHONPATH set to $env:PYTHONPATH"
