
import smtplib
from app2.app.config import config

def task1_(email: str):
    with smtplib.SMTP('smtp.gmail.com', 587)as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        print(config.SMTP_SENDER)
        print(config.SMTP_PASSWORD)

        smtp.login(config.SMTP_SENDER, config.SMTP_PASSWORD)
        print("SENDING EMAIL...")
        subject = 'welcome to out website'
        body = 'welcome to our book tracker website'
        msg= f'subject: {subject}\n\n{body}'

        smtp.sendmail(config.SMTP_SENDER, email, msg)
