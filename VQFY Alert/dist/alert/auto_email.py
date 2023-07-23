import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up your smtp here

def email(message):
    # Set up the SMTP server details
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = ''
    smtp_password = ''

    # Set up the email content
    sender_email = ''
    sender_name = 'VQFY Alert'
    receiver_email = input("Please input the e-mail in which you wish to receive the alert: ")
    print('\n')
    print('Sending...')
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
