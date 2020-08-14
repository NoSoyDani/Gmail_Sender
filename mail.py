from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def mailSender(source,passw,target,subject,message):
   msg = MIMEMultipart()
   msg['From'] = source
   msg['To'] = target
   msg['Subject'] = subject
   msg.attach(MIMEText(message, 'plain'))
   server = smtplib.SMTP('smtp.gmail.com: 587')
   server.starttls()
   server.login(source, passw)
   server.sendmail(msg['From'], msg['To'], msg.as_string())
   server.quit()
