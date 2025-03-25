$SMTPServer = "smtp.gmail.com"
$SMTPPort = "587"

$Username = "osmanharald5@gmail.com"
$Password = "ovsbxveiojwtoncn"

$From = "osmanharald5@gmail.com"
$To = "osmanharald5@gmail.com"
$Subject = "Get Trolled"
$Body = "---------------Troll---------------"

$SMTPClient = New-Object Net.Mail.SmtpClient($SMTPServer, $SMTPPort)
$SMTPClient.EnableSsl = $true
$SMTPClient.Credentials = New-Object System.Net.NetworkCredential($Username, $Password)

$MailMessage = New-Object Net.Mail.MailMessage($From, $To, $Subject, $Body)

$SMTPClient.Send($MailMessage)
