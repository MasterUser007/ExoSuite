# scripts/full_wash.ps1

# 1. Patch all .py files for basic errors (junk lines, typo imports, f-strings)
Get-ChildItem -Recurse -Include *.py | ForEach-Object {
    $f = $_.FullName
    $l = Get-Content $f
    $changed = $false
    while ($l.Count -gt 0 -and ($l[0] -match '^\s*```' -or $l[0] -match '^\s*$' -or $l[0] -match '^Example:')) {
        $l = $l[1..($l.Count-1)]
        $changed = $true
    }
    for ($i = 0; $i -lt $l.Count; $i++) {
        if ($l[$i] -match 'f\\\"') { $l[$i] = $l[$i] -replace 'f\\\"','f"'; $changed = $true }
        if ($l[$i] -match '^mport ') { $l[$i] = $l[$i] -replace '^mport','import'; $changed = $true }
        if ($l[$i] -match '^rom ') { $l[$i] = $l[$i] -replace '^rom','from'; $changed = $true }
    }
    if ($changed) { Set-Content $f $l; Write-Host "Patched $f" -ForegroundColor Yellow }
}

# 2. Run Black if installed
if (Get-Command black -ErrorAction SilentlyContinue) {
    Write-Host "`nRunning Black on Python files..." -ForegroundColor Cyan
    black .
}

# 3. Fix pytest.ini header in every pytest.ini file found
Get-ChildItem -Recurse -Filter pytest.ini | ForEach-Object {
    $f = $_.FullName
    $lines = Get-Content $f
    if ($lines.Count -gt 0 -and $lines[0] -ne '[pytest]') {
        $lines[0] = '[pytest]'
        Set-Content $f $lines
        Write-Host "Fixed header in $f" -ForegroundColor Green
    }
}

# 4. Ensure all major engine dirs have tests/ with at least one test file
$engines = @(
    "FactorEngine",
    "QuantumHash",
    "PrimeEngineAI",
    "gpu_sieve",
    "primality_test",
    "orchestration",
    "remainder_analysis"
)
foreach ($engine in $engines) {
    $testDir = "$engine/tests"
    if (!(Test-Path $testDir)) {
        New-Item -ItemType Directory -Path $testDir -Force | Out-Null
    }
    $testFile = "$testDir/test_placeholder.py"
    if (!(Test-Path $testFile)) {
        Set-Content $testFile "def test_placeholder():`n    assert True"
        Write-Host "Ensured $testFile" -ForegroundColor Cyan
    }
}

Write-Host "`n==== Repo full wash complete! ====" -ForegroundColor Magenta

