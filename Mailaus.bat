@echo off
:loop
    powershell -ExecutionPolicy Bypass -File "%cd%\Mailspam.ps1"
    echo ------------------------------------------------ fertig-----------------------------
goto loop
