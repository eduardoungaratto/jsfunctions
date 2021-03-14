from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
import mimetypes
import email.mime.application
from datetime import datetime
import time

# before you use this script, allow on google account, the option for less secure apps

G_SERVER = None

# Fill with your gmail account.
_name = ''
_user = ''
_pass = ''

# Fill with your text
_body = ''
_subject = ''
_file = ''

email_to = []
contact_list = 'YOUR FILE CONTACT LIST'
file=open(contact_list,'r', encoding='utf-8')
txt = file.read()
email_to = txt.split(',')
file.close()

# Conteudo da email
html = """PASTE HOUR HTML HERE"""

def start_server():
  try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
  except Exception as e:
    print('exc -> %s', e)
  return server

def connect_server(server, email_user, email_pass):
  try:
    server.login(email_user, email_pass)  
  except Exception as e:
    print('connect_server exc -> %s', e)
  return server

def disconnect_server(server):
  try:
    server.quit() 
  except Exception as e:
    print('disconnect_server exc -> %s', e)

def new_email(_name, html, _subject, _to):
  try:
    # Send message with html on email body
    content = MIMEText(html, "html")
    msg = MIMEMultipart("alternative")
    msg['Subject'] = _subject
    msg['From'] = _name
    msg['To'] = _to
    msg.attach(content)
  except Exception as e:
    print('new_email exc -> %s', e)
  return msg

def sender(server, msg):
  try:
    print('sending message for  -> %s', msg['To'])
    server.send_message(msg)
    with open('log_run_' +  datetime.now().strftime("%d_%m_%y") + '.txt', 'a+', encoding='utf-8') as logfile:
      logfile.write("sending message for :" + str(to) + " em " + datetime.now().strftime("%d/%m/%y %H:%M:%S \n"))
    time.sleep(10)
  except Exception as e:
    print('sender exc -> %s', e)
    raise e
  return server

def shoting_up(server, _name, html, _subject, to):
  try:
    msg = new_email(_name, html, _subject, to)
    sender(server, msg)
  except Exception as e:
    print('shoting_up exc -> %s', e)
    raise e

def gunner(server, _name, html, _subject):
  try:
    continue_runner = True
    size_email_to = len(email_to)
    index = 0
    last_index = 0
    size_list = 0
    
    for index in range(size_email_to):
      size_list = index + 1

    last = 'last_index.txt'
    last=open(last,'r', encoding='utf-8')
    txt_index = last.read()
    last.close()
    index = int(txt_index)
    print('index -> %s', index)
    print('size_list -> %s', size_list)

    while index <= size_list:
      print("index position in size_list -> %s", index)
      to = email_to[index]
      shoting_up(server, _name, html, _subject, to)
      index = index + 1
      last_index = index
      with open('last_index.txt', 'w', encoding='utf-8') as logfile:
        logfile.write(str(last_index))

    with open('log_end_' + datetime.now().strftime("%d_%m_%y") + '.txt', 'a+', encoding='utf-8') as logfile:
        logfile.write("shots amount : " + str(last_index) + " em " + datetime.now().strftime("%d/%m/%y %H:%M:%S \n"))

    if index >= size_list:
      continue_runner = False

  except Exception as e:
    print('gunner exc -> %s', e)
    raise e
  return continue_runner

def runner(power):
  try:
    server = start_server()
    server = connect_server(server, _user, _pass)

    while power: 
      time.sleep(30)
      power = gunner(server, _name, html, _subject)
      G_SERVER = server

    disconnect_server(server)
    print("The runner arrives at end, power -> %s", power)
  except Exception as e:
    print('The runner found a problem exc -> %s', e)
    raise e

try:
  runner(power=True)
except Exception as e:
  print('An exc was occurred -> %s', e)
  disconnect_server(G_SERVER)
  runner(power=False)
