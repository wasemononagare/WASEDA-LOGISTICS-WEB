@echo off
chcp 65001 > nul
echo ==============================================
echo   GitHub Push Script (WASEDA-LOGISTICS-WEB)
echo ==============================================

set GIT="C:\Users\yumu0\AppData\Local\Programs\PortableGit\cmd\git.exe"

cd /d "%~dp0\.."

echo [1/3] Checking Git status...
%GIT% status

echo.
echo [2/3] Adding changes and committing...
%GIT% add .
%GIT% commit -m "Update site content"

echo.
echo [3/3] Pushing to GitHub (main)...
%GIT% -c credential.helper= push origin main

echo.
if %ERRORLEVEL% EQU 0 (
    echo ==============================================
    echo   Push successful! (GitHubに正常に反映されました)
    echo ==============================================
) else (
    echo ==============================================
    echo   Push failed. Please check the error above.
    echo ==============================================
)

pause
