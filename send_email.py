from email.mime.text import MIMEText
import smtplib


def send_email(email, height, average_height, count):
    from_email = "vg11072001@students.vnit.ac.in"
    from_password = "BT19MIN045"
    to_email= email

    subject = "Height data"
    message = "Hey there, you height is <strong> %s </strong>. And average height of all is <strong> %s </strong> which is claculated out of  <strong> %s </strong>! " % (height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
