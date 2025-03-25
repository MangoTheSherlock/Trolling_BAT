@echo off
:loop
    powershell -ExecutionPolicy Bypass -File "%cd%\Mailspam.ps1"
    echo Ausfuehrung %%i von %count% abgeschlossen.

echo Alle %count% Ausfuehrungen des PowerShell-Skripts wurden abgeschlossen!
goto loop
