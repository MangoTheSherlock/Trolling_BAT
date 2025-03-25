import smtplib
import os
import time
import socket
import requests
from email.message import EmailMessage

# 🔹 1. Eigene IP-Adresse ermitteln
def get_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)  # Lokale IP
        public_ip = requests.get("https://api64.ipify.org").text  # Öffentliche IP
        return hostname, local_ip, public_ip
    except Exception as e:
        return "Fehler", "Nicht gefunden", str(e)

hostname, local_ip, public_ip = get_ip()

# 🔹 2. Datei erstellen
file_path = os.path.expanduser("~/Desktop/output.txt")  # Datei auf dem Desktop
file_name = "output.txt"

with open(file_path, "w") as file:
    file.write(f"Hostname: {hostname}\n")
    file.write(f"Lokale IP: {local_ip}\n")
    file.write(f"Öffentliche IP: {public_ip}\n")
    file.write(f"Erstellt am: {time.ctime()}\n")

print(f"📄 Datei '{file_name}' wurde erstellt!")

# 🔹 3. E-Mail-Daten einrichten
EMAIL_ABSENDER = "osmanharald5@gmail.com"   # <== Deine E-Mail hier eintragen
EMAIL_PASSWORT = "Empfangen"       # <== App-Passwort hier eintragen
EMAIL_EMPFAENGER = "osmanharald5@gmail.com"  # <== Empfänger-E-Mail hier eintragen

# 🔹 4. E-Mail mit Anhang senden
msg = EmailMessage()
msg["Subject"] = "IP-Informationen"
msg["From"] = EMAIL_ABSENDER
msg["To"] = EMAIL_EMPFAENGER
msg.set_content("Hier ist die Datei mit den IP-Informationen.")

# Datei als Anhang hinzufügen
with open(file_path, "rb") as file:
    msg.add_attachment(file.read(), maintype="text", subtype="plain", filename=file_name)

try:
    # SMTP-Server verbinden (Google SMTP)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ABSENDER, EMAIL_PASSWORT)
        server.send_message(msg)
    
    print("✅ E-Mail mit Anhang erfolgreich gesendet!")
except Exception as e:
    print(f"❌ Fehler beim Senden der E-Mail: {e}")

# 🔹 5. Datei vom Desktop löschen
os.remove(file_path)
print(f"🗑️ Datei '{file_name}' wurde vom Desktop gelöscht!")
