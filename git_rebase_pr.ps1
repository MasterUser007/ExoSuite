# --- Automated Git workflow for protected branch with rebasing and PR ---

param (
    [string]$WorkingBranch = "rebase-fix-branch-2",
    [string]$BaseBranch = "main"
)

function Prompt-ManualConflictFix {
    Write-Host "`n[!] Merge conflicts detected during rebase."
    Write-Host "Please resolve conflicts manually in your editor."
    Write-Host "After resolving, stage files with 'git add <file>' and run 'git rebase --continue'."
    Write-Host "Press Enter when ready to continue or Ctrl+C to abort."
    Read-Host
}

# Checkout working branch or create it if missing
if (-not (git show-ref --verify --quiet refs/heads/$WorkingBranch)) {
    Write-Host "Branch '$WorkingBranch' does not exist locally. Creating it from $BaseBranch."
    git checkout -b $WorkingBranch origin/$BaseBranch
} else {
    git checkout $WorkingBranch
}

# Fetch latest changes
git fetch origin

# Rebase working branch onto latest base branch
while ($true) {
    $rebaseOutput = git rebase origin/$BaseBranch 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[+] Rebase successful!"
        break
    } elseif ($rebaseOutput -match "CONFLICT") {
        Prompt-ManualConflictFix
    } else {
        Write-Error "Unexpected rebase error: $rebaseOutput"
        exit 1
    }
}

# Push branch to origin with force-with-lease
git push --force-with-lease origin $WorkingBranch

# Create Pull Request with GitHub CLI, open in browser
Write-Host "Opening Pull Request page for branch '$WorkingBranch'..."
gh pr create --base $BaseBranch --head $WorkingBranch --title "Sync with $BaseBranch - Automated Rebase" --body "Automated rebase and sync with $BaseBranch." --web

Write-Host "`n---"
Write-Host "Next steps:"
Write-Host "- Review and merge the Pull Request on GitHub."
Write-Host "- After merge, sync your local main branch with:"
Write-Host "    git checkout $BaseBranch"
Write-Host "    git pull origin $BaseBranch"