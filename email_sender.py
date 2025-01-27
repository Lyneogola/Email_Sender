from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'lyneogola@gmail.com'
emai_password = 'enter your passkey'

email_receiver = 'rovoko1451@citdaca.com'

subject = 'Test'
body = '''
Testing my code
'''

em = EmailMessage()
em['From']  = email_sender
em['To']=email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, emai_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

