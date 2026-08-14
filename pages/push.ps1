$git = "C:\Users\yumu0\AppData\Local\Programs\PortableGit\cmd\git.exe"

Set-Location (Join-Path $PSScriptRoot "..")

Write-Host "=== 1. Checking Git Status ===" -ForegroundColor Cyan
& $git status

Write-Host "`n=== 2. Staging & Committing Changes ===" -ForegroundColor Cyan
& $git add .
$status = & $git status --porcelain
if ($status) {
    & $git commit -m "Update site content"
    Write-Host "Changes committed." -ForegroundColor Green
} else {
    Write-Host "No changes to commit." -ForegroundColor Yellow
}

Write-Host "`n=== 3. Pushing to GitHub (origin/main) ===" -ForegroundColor Cyan
& $git -c credential.helper= push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n[SUCCESS] Push successfully completed!" -ForegroundColor Green
} else {
    Write-Host "`n[ERROR] Push failed." -ForegroundColor Red
}
