@echo off
cd %TEMP%
echo Lade Python-Skript von GitHub herunter...

curl -L -o Troll2.py "https://raw.githubusercontent.com/MangoTheSherlock/Trolling_BAT/main/Troll2.py"

echo Download abgeschlossen. Starte das Skript...
python Troll2.py
exit