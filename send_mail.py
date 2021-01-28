import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'a94c5e8b9afae9'
    password = 'e18ead6030272d'
    message = f'''\<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li>
    <li>Dealer: {dealer}</li><li>Rating: {rating}</li>
    <li>Comments: {comments}</li></ul>'''

    sender_email = 'email1@example.com' # your domain
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Feedback form'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())