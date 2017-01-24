import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("alam.tahmid@gmail.com","YouareabadboY")

msg = "This is test mail"
server.sendmail("alam.tahmid@gmail.com","alam.tamzid@live.com",msg)
server.quit()