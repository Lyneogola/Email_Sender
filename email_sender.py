from email.message import EmailMessage
import ssl
import smtplib
import socket

# Function to validate email domain
def is_valid_domain(email):
    try:
        domain = email.split('@')[1]
        socket.gethostbyname(domain)  # Resolves the domain to an IP
        return True
    except (IndexError, socket.gaierror):
        return False

# Sender email credentials
email_sender = 'lyneogola@gmail.com'
emai_password = 'enter passkey'

# Prompt for receiver's email
email_receiver = input("Enter receiver's email: ")

# Validate domain before proceeding
if not is_valid_domain(email_receiver):
    print(f"❌ The domain for {email_receiver} could not be resolved. Check for typos or invalid domain names.")
else:
    # Email content
    subject = 'Test'
    body = '''
    Testing my code
    '''

    # Create the email message
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Create SSL context
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, emai_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        print(f"✅ Email sent successfully to {email_receiver}")
    except smtplib.SMTPRecipientsRefused:
        print(f"❌ The email address {email_receiver} is invalid or not reachable.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
