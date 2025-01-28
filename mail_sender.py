from email.message import EmailMessage
import ssl
import smtplib

# Define sender and receiver email addresses
email_sender = 'lyne.ogola@cloudproductivity-solutions.com'
#emai_password = 'pxak tjgb mjim txua'
email_receiver = input("Enter receiver's email: ")

# Email subject and body
subject = 'Test'
body = '''
This is a code written email
'''

# Create an EmailMessage instance
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Create a secure SSL context
context = ssl.create_default_context()

# Send the email using SMTP_SSL
try:
    with smtplib.SMTP('smtp.office365.com',587) as smtp:
        smtp.starttls(context=context)
        smtp.login(email_sender,'Kefri@23')
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
