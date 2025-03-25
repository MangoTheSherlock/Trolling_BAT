@echo off
setlocal enabledelayedexpansion

set /a count=0

:loop
    set /a count+=1
    start /b powershell -ExecutionPolicy Bypass -File "%cd%\Mailspam.ps1"
    echo ------------------------------------------------ fertig-----------------------------
    echo Anzahl der Ausführungen: !count!
    timeout /t 1 /nobreak >nul
goto loop
