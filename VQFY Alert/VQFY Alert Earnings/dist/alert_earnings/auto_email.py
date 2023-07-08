import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def email(message):
    
    # Set up the SMTP server details
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'stockalerthsc@gmail.com'
    smtp_password = 'hxcunirmyzoxmuwg'

    # Set up the email content
    sender_email = 'stockalerthsc@gmail.com'
    sender_name = 'VQFY Alert'
    receiver_email = input('Please input the e-mail in which you wish to receive the alert: ')
    subject = 'Today\'s winners/losers'

    # Create a multipart message and set the appropriate headers
    msg = MIMEMultipart()
    msg['From'] = f'{sender_name} <{sender_email}>'
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

        return
