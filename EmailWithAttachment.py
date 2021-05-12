from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import mimetypes
import email.mime.application
from datetime import datetime


_name = ''
_user = ''
_pass = ''
_body = ''
_subject = ''
_file = ''

email_to = []
contatos = 'contatos.txt'
file=open(contatos,'r', encoding='utf-8')
txt = file.read()
email_to = txt.split(',')
file.close()

def to_send(email_user, email_pass, msg, to):
	try:
		s = smtplib.SMTP('smtp.gmail.com:587')
		s.starttls()
		s.login(email_user, email_pass)

		print("Enviando para: " + to)
		
		s.send_message(msg)
		s.quit()	
	except Exception as e:
		raise e



def new_email(_name, _user, _pass, _body, _subject, _file, to):

	email_name = _name
	email_user = _user
	email_pass = _pass
	email_body = _body
	email_subject = _subject
	email_file = _file


	fot=open(email_body,'r', encoding='utf-8')
	txt = fot.read()
	fot.close()
	txt = str(txt)

	msg = MIMEMultipart()
	msg['Subject'] = email_subject
	msg['From'] = email_name
	msg['To'] = to

	txt = MIMEText(txt)
	msg.attach(txt)

	filename = email_file
	fo=open(filename,'rb')
	attach = email.mime.application.MIMEApplication(fo.read(),_subtype="pdf")
	fo.close()
	
	attach.add_header('Content-Disposition','attachment',filename=filename)
	msg.attach(attach)
	
	to_send(email_user, email_pass, msg, to);


size_email_to = len(email_to)
index = 0
for index in range(size_email_to):
	to = email_to[index]
	new_email(_name, _user, _pass, _body, _subject, _file, str(to))
	index = index + 1;

print("Total enviado foi: " + str(index) + " em " + datetime.now().strftime("%d/%m/%y %H:%M:%S \n"))
with open('log.txt', 'a', encoding='utf-8') as logfile:
    logfile.write("Total enviado foi: " + str(index) + " em " + datetime.now().strftime("%d/%m/%y %H:%M:%S \n"))
