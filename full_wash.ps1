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
