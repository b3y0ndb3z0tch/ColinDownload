import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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

def email_alert_table(recipient, subject, body):
    msg = MIMEMultipart('alternative')
    msg['to'] = recipient
    msg['from']= "Bah.hockey@gmail.com"
    msg['subject'] = subject
    part = MIMEText(body, 'html')
    msg.attach(part)

    user = "Bah.Hockey@gmail.com"
    password = "eufffmhkdyoaewug"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

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

def specific_player_info(**kwargs):
    for a in kwargs:
        print(a)

if __name__=='__main__':
    cellnumbers = ["18582318394"]
    list = ['txt.att.net', 'sms.myboostmobile.com', 'mms.cricketwireless.net', 'msg.fi.google.com', \
            'text.republicwireless.com', 'vtext.com', \
            'email.uscc.net', 'vtext.com', 'mms.att.net', \
            'myboostmobile.com', 'mms.cricketwireless.net', 'msg.fi.google.com', 'pm.sprint.com',\
            'mypixmessages.com', 'tmomail.net', 'mmst5.tracfone.com', 'mms.uscc.net', 'vzwpix.com'\
            'vmpix.com']
    for cell in cellnumbers:
        for i in list:
            recipient = str(cell+"@"+i)
            message = str("I just sent this text message using all the available services I can find at the moment.  \
            Let me know what this is: " + i)
            print(recipient)
            text_alert(recipient, "Automated List Test Text", message)

    # email_address = ["adamwilliams86@yahoo.com", "chosegood@gmail.com"]
    # for address in email_address:
    #     email_alert(address, "Automated List Test Email", "Just checking the automation email")


