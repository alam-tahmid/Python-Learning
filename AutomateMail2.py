import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromAddress = "alam.tahmid@gmail.com"
password = "YouareabadboY"
print("Enter email Id")
toAddress = input()

msg = MIMEMultipart()
msg['From'] = fromAddress
msg['To'] = toAddress
print('Enter Subject')
msg['Subject'] = input()
print("Body of the message")
body = input()
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromAddress,password)
text = msg.as_string()
server.sendmail(fromAddress,toAddress,text)
server.quit()
print("Email has been sent")