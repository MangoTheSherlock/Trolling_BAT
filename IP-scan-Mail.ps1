# PowerShell E-Mail-Skript

# SMTP-Server von Google
$SMTPServer = "smtp.gmail.com"
$SMTPPort = "587"

# Deine Anmeldedaten (Google-Adresse und App-Passwort)
$Username = "osmanharald5@gmail.com"
$Password = "ovsbxveiojwtoncn"

# E-Mail Details
$From = "osmanharald5@gmail.com"
$To = "osmanharald5@gmail.com"  # Empfängeradresse (kann auch eine andere sein)
$Subject = "Test E-Mail von PowerShell"
$Body = "Hallo, dies ist eine automatisch gesendete E-Mail aus einem PowerShell-Skript."

# SMTP Client erstellen und konfigurieren
$SMTPClient = New-Object Net.Mail.SmtpClient($SMTPServer, $SMTPPort)
$SMTPClient.EnableSsl = $true
$SMTPClient.Credentials = New-Object System.Net.NetworkCredential($Username, $Password)

# E-Mail senden
$SMTPClient.Send($From, $To, $Subject, $Body)

# Erfolgsmeldung
Write-Output "E-Mail erfolgreich gesendet!"
