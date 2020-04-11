import smtplib
from email.mime.text import MIMEText


def send_mail(name, email, phone, message):
    port = 2525
    smtp_server = 'smtp.elasticemail.com'
    login = ''
    password = ''
    message = f"<h3>New DITE IIF feedback Submission</h3><ul><li>Name: {name}</li><li>E-mail: {email}</li><li>Phone no: {phone}</li><li>message: {message}</li></ul>"

    sender_email = ''
    receiver_email = ''
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'DITE IFF Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
