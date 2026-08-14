@echo off
chcp 65001 > nul
cd /d "%~dp0"
echo [Sync] Checking for remote updates...
"C:\Users\yumu0\AppData\Local\Programs\PortableGit\cmd\git.exe" pull origin main --rebase
echo [Sync] Staging all changes...
"C:\Users\yumu0\AppData\Local\Programs\PortableGit\cmd\git.exe" add .
set /p commit_msg="Enter commit message (or press enter for default 'Update site content'): "
if "%commit_msg%"=="" set commit_msg=Update site content
echo [Sync] Committing: %commit_msg%
"C:\Users\yumu0\AppData\Local\Programs\PortableGit\cmd\git.exe" commit -m "%commit_msg%"
echo [Sync] Pushing to GitHub...
"C:\Users\yumu0\AppData\Local\Programs\PortableGit\cmd\git.exe" push origin main
echo.
echo ====================================================
echo  GitHub縺ｸ縺ｮ繝励ャ繧ｷ繝･縺悟ｮ御ｺ・＠縺ｾ縺励◆・・echo ====================================================
pause