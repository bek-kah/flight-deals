import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class NotificationManager:
    def __init__(self):
        self.me = 'bekpython@gmail.com'
        # Email it's going to
        self.you = 'ulugbek7767@gmail.com'
        self.password = 'ztmgvhxayqrpuqew'

    def send_email(self, body):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=self.me, password=self.password)
            connection.sendmail(self.me, self.you, msg=f'Subject: Ticket Alert!\n\n{body}')
