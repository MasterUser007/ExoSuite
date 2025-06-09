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
