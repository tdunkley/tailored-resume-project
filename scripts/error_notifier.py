import logging
import smtplib
from email.mime.text import MIMEText

# ...existing code...

def send_error_notification(subject, body, to_email):
    """Send an error notification email."""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'noreply@example.com'
    msg['To'] = to_email

    with smtplib.SMTP('smtp.example.com') as server:
        server.send_message(msg)
    logging.info(f"Sent error notification to {to_email}")

# ...existing code...
