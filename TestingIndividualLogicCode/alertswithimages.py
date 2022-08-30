from datetime import datetime
from email.message import EmailMessage
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

cellnumbers = ["18582318394"]
cell_tower_list = ['txt.att.net', 'msg.fi.google.com', 'text.republicwireless.com', 'vtext.com', 'tmomail.net', \
        'email.uscc.net', 'vtext.com', 'vmobl.com', 'mms.att.net', 'myboostmobile.com', 'mms.cricketwireless.net', \
        'msg.fi.google.com', 'mypixmessages.com', 'tmomail.net', 'mmst5.tracfone.com', 'mms.uscc.net', 'vzwpix.com' \
        'vmpix.com']


def email_alert(recipient, subject, body):
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

def text_alert(recipient, subject, body, attach_file):
    msg = MIMEMultipart()
    msg.attach(MIMEText(body,'plain'))
    if attach_file != "":
        fp = open(attach_file, 'rb')
        msg_img = MIMEImage(fp.read())
        fp.close()
        msg.attach(msg_img)
    msg['To'] = recipient
    msg['From']= "Bah.hockey@gmail.com"
    msg['Subject'] = subject
    # msg.set_content(body)

    user = "Bah.Hockey@gmail.com"
    password = "eufffmhkdyoaewug"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)

    server.send_message(msg)
    server.quit()

if __name__=='__main__':

    for cell in cellnumbers:
        for i in cell_tower_list:
            recipient = str(cell+"@"+i)
            message = str("I just sent this text message using all the available services I can find at the moment.  \
            Let me know what this is: " + i)
            print(recipient)
            text_alert(recipient, "Automated List Test Text", message, 'BAHlogo.jpeg')

    # email_address = ["adamwilliams86@yahoo.com", "chosegood@gmail.com"]
    # for address in email_address:
    #     email_alert(address, "Automated List Test Email", "Just checking the automation email")


