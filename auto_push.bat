@echo off
chcp 65001 > nul
cd /d "%~dp0"
echo [Sync] Checking for remote updates...
"C:\Program Files\Git\cmd\git.exe" pull origin main --rebase
echo [Sync] Staging all changes...
"C:\Program Files\Git\cmd\git.exe" add .
set /p commit_msg="Enter commit message (or press enter for default 'Update site content'): "
if "%commit_msg%"=="" set commit_msg=Update site content
echo [Sync] Committing: %commit_msg%
"C:\Program Files\Git\cmd\git.exe" commit -m "%commit_msg%"
echo [Sync] Pushing to GitHub...
"C:\Program Files\Git\cmd\git.exe" push origin main
echo.
echo ====================================================
echo  GitHubへのプッシュが完了しました！
echo ====================================================
pause