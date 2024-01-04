# dict1 = {1:'donkey', 2:'chicken'}
# dict2 = {1:'donkey', 2:'chickenn'}
# set1 = set(dict1.items())
# set2 = set(dict2.items())
# diff = (set2 - set1)
# message = "HOUSE SCRAPERS - You have the following changes:"
# for d in diff:
#     l = list(d)
#     message += "\n"+l[0]+"is changed from"+l[1]




def sendemail():
    import smtplib

    sender = 'nl3842403@gmail.com'
    receivers = ['shoaibsivany@gmail.com']

    message = """From: From Person <nl3842403@gmail.com.com>
    To: To Person <to@todomain.com>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)         
        print ("Successfully sent email")
    except Exception as e:
        print ("Error: unable to send email",e)


def sendem2():
    # Import smtplib for the actual sending function
    import smtplib

    # Here are the email package modules we'll need
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart

    # Create the container (outer) email message.
    msg = MIMEMultipart()
    msg['Subject'] = 'Our family reunion'
    me = 'nl3842403@gmail.com'
    family = 'nl3842403@gmail.com'
    msg['From'] = me
    msg['To'] = ', '.join(family)
    msg.preamble = 'Our family reunion'

    

    # Send the email via our own SMTP server.
    s = smtplib.SMTP('localhost')
    s.sendmail(me, family, msg.as_string())
    s.quit()

def sendy():
    
    import yagmail
    
    yagmail.register('nl3842403@gmail.com', 'nanalala123')
    
    yag = yagmail.SMTP()
    contents = [
        "This is the body, and here is just text http://somedomain/image.png",
        "You can find an audio file attached"
    ]
  
    # Alternatively, with a simple one-liner:
    yagmail.SMTP('nl3842403@gmail.com').send('nl3842403@gmail.com', 'subject', contents)

sendy()


