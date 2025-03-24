import subprocess

# Befehl ausführen und Ausgabe erfassen
result = subprocess.run("ipconfig", shell=True, capture_output=True, text=True)

# Konsolenausgabe speichern
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(result.stdout)

print("Die IP-Informationen wurden in 'output.txt' gespeichert.")
