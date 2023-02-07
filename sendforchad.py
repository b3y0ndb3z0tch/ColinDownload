import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

def text_alert(recipient, subject, body):
    msg = EmailMessage()
    msg['to'] = recipient
    msg['from']= "Bah.hockey@gmail.com"
    msg['subject'] = subject
    msg.set_content(body)

    user = "Bah.Hockey@gmail.com"
    password = "eufffmhkdyoaewug"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

list = ['txt.att.net', 'sms.myboostmobile.com', 'mms.cricketwireless.net', 'msg.fi.google.com', \
            'text.republicwireless.com', 'vtext.com', \
            'email.uscc.net', 'vtext.com', 'mms.att.net', \
            'myboostmobile.com', 'mms.cricketwireless.net', 'msg.fi.google.com', 'pm.sprint.com',\
            'mypixmessages.com', 'tmomail.net', 'mmst5.tracfone.com', 'mms.uscc.net', 'vzwpix.com'\
            'vmpix.com']
with open('ContactInfo.json') as allcontactinfo:
    all_contact_info = json.load(allcontactinfo)
    for player in all_contact_info:
        if player["LINE"] == "1" or player["LINE"] == "1 2":
            for i in list:
                text_alert(player["Cell Number"]+"@"+i, "TONIGHT SKATE", "NEED A PLAYER TONIGHT 10:30PM UTC RESPOND ASAP CALL OR TEXT Chad Hosegood @ 8609770538")



