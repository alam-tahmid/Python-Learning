import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromAddress = 'alam.tahmid@gmail.com'
password = 'YouareabadboY'
toAddress = input('Enter email id:')

msg = MIMEMultipart()
msg['From'] = fromAddress
msg['To'] = toAddress
msg['Subject'] = input('Subject: \n')

fr = open('EmailBody.txt','r')
body = fr.read()
msg.attach(MIMEText(body,'plain'))
filename = input('File Name: \n')
attachment = open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Diposition',"attachment; fileName= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromAddress,password)
text = msg.as_string()
server.sendmail(fromAddress,toAddress,text)
server.quit()
print('Done!')

