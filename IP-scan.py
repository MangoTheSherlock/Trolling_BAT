from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import time

file_path = os.path.expanduser("~/Desktop/output.txt")
file_name = "output.txt"

with open(file_path, "w") as file:
    file.write("Hallo, das ist eine automatisch erstellte Datei!\n")
    file.write(f"Erstellt am: {time.ctime()}\n")

print(f"📄 Datei '{file_name}' wurde auf dem Desktop erstellt!")

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

folder_id = "1zLRe3Kq1x4FDB5khIUTHaHMA9-feiHRf"

file = drive.CreateFile({'title': file_name, 'parents': [{'id': folder_id}]})
file.SetContentFile(file_path)
file.Upload()
print(f"✅ Datei '{file_name}' wurde in Google Drive hochgeladen! (Ordner-ID: {folder_id})")

os.remove(file_path)
print(f"🗑️ Datei '{file_name}' wurde vom Desktop gelöscht!")
