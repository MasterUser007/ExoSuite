# test_then_prompt.ps1
Write-Host "===== REPOSITORY TEST DRY RUN =====" -ForegroundColor Cyan

# Step 1: Run Tests
Write-Host "`nRunning pytest..." -ForegroundColor Yellow
$pytestResult = python -m pytest
if ($LASTEXITCODE -eq 0) {
    Write-Host "`n[PASS] All tests succeeded." -ForegroundColor Green
} else {
    Write-Host "`n[FAIL] Some tests failed. Check output above." -ForegroundColor Red
}

# Step 2: Ask for next steps
$choice = Read-Host "`nNext steps? (enter: wash, build, ci, push, quit)"
switch ($choice.ToLower()) {
    "wash" {
        Write-Host "`nRunning repo wash..." -ForegroundColor Yellow
        ./scripts/full_wash.ps1
    }
    "build" {
        Write-Host "`nRunning build (if applicable)..." -ForegroundColor Yellow
        # Example build command; replace if different:
        python setup.py build
    }
    "ci" {
        Write-Host "`nRunning CI workflow (GitHub Actions, etc)..." -ForegroundColor Yellow
        # Simulate CI: e.g., run scripts/ci_check.ps1 if you have one
        ./scripts/ci_check.ps1
    }
    "push" {
        Write-Host "`nPushing all branches to remote..." -ForegroundColor Yellow
        $branches = git for-each-ref --format="%(refname:short)" refs/heads/ | ForEach-Object { $_.Trim() }
        foreach ($branch in $branches) {
            git push origin $branch
        }
    }
    "quit" {
        Write-Host "Exiting script." -ForegroundColor Cyan
        exit 0
    }
    default {
        Write-Host "Unknown option. Exiting." -ForegroundColor Red
        exit 1
    }
}
