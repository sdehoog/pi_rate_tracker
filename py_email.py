import os
import smtplib
from dotenv import load_dotenv

load_dotenv()
FROM_PASS = os.getenv('FROM_PASS')
FROM_EMAIL = os.getenv('FROM_EMAIL')
TO_EMAIL = os.getenv('TO_EMAIL')


def send_email(subj='Howdy', body='Test'):
    with smtplib.SMTP('smtp.mail.yahoo.com', 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()
        connection.login(user=FROM_EMAIL, password=FROM_PASS)
        connection.sendmail(from_addr=FROM_EMAIL, to_addrs=TO_EMAIL,
                            msg=f'Subject:{subj}\n\n{body}')


if __name__ == '__main__':
    send_email()
