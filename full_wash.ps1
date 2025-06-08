<<<<<<< HEAD
param([switch]$CommitAutoFixes)

Set-StrictMode -Version Latest

if (-not (Test-Path .gitattributes)) {
  "*.ps1 text eol=crlf`n*.sh  text eol=lf`n*    text=auto" | Set-Content .gitattributes -Encoding UTF8 -NoNewline
}

git ls-files --ignored --exclude-standard -z |
  ForEach-Object { git rm --cached --ignore-unmatch -- $_ }

Get-ChildItem -Recurse -Filter '*.py' | ForEach-Object {
  $init = Join-Path $_.DirectoryName '__init__.py'
  if (-not (Test-Path $init)) { New-Item -ItemType File -Path $init -Force | Out-Null }
}

& black --check .      || throw 'Black formatting check failed'
& isort --check-only . || throw 'isort import sort check failed'
& flake8 .             || throw 'flake8 linting failed'

if (-not (Get-Module -ListAvailable -Name PSScriptAnalyzer)) {
  Install-Module -Name PSScriptAnalyzer -Force -Scope CurrentUser
}
Invoke-ScriptAnalyzer -Recurse || throw 'PSScriptAnalyzer reported issues'

git clean -n -xfd
git clean -f -xfd

if ($CommitAutoFixes) {
  git add .
  git commit -m 'chore: full wash auto-fixes'
}

Write-Host '✅ Full wash passed – ready to commit'
=======
<#
.SYNOPSIS Full workspace wash
.DESCRIPTION
  - Resets Git (if present)
  - Deletes caches, venvs, builds, IDE folders, OS junk
#>
if (Test-Path .git) { git reset --hard; git clean -xdf }
Get-ChildItem -Recurse -Include *.pyc,*.pyo | Remove-Item -Force -ErrorAction SilentlyContinue
Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
@("venv",".venv","__venv__") | % { if (Test-Path ) { Remove-Item  -Recurse -Force }}
@("build","dist") | % { if (Test-Path ) { Remove-Item  -Recurse -Force }}
Get-ChildItem -Recurse -Directory -Filter "*.egg-info" | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
@(".pytest_cache","htmlcov",".coverage") | % { if (Test-Path ) { Remove-Item  -Recurse -Force }}
if (Test-Path "node_modules") { Remove-Item node_modules -Recurse -Force }
@(".idea",".vscode",".vs") | % { if (Test-Path ) { Remove-Item  -Recurse -Force }}
Get-ChildItem -Recurse -Include Thumbs.db,".DS_Store","*.bak","*~" | Remove-Item -Force -ErrorAction SilentlyContinue
Remove-Item -Path "C:\Users\leebo\AppData\Local\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "C:\Windows\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "C:\Windows\Prefetch\*" -Recurse -Force -ErrorAction SilentlyContinue
Write-Host "✅ Full wash complete." -ForegroundColor Green
>>>>>>> 3453edc (chore(repo): full monorepo restructure, test/config updates, and CI setup)
