import os
import smtplib
import requests

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMETEXT import MIMETEXT
from email import Encoders


'''
USING SMTP
'''

EMAIL_HOST_SERVER = smtp.SMTP('smtp.gmail.com', 587)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'eventbuzzer@gmail.com'
DEFAULT_FROM_EMAIL = 'eventbuzzer@gmail.com'
EMAIL_HOST_PASSWORD = 'Shellshocked'


# attachment is a ticket(ticket data, i.e ticket no, with event details)
def mail(to, subject, text, attach, attachment):
	msg = MIMEMultipart()
	msg['From'] = EMAIL_HOST_USER
	msg['To'] = to
	msg['Subject'] = subject
	msg.attach(MIMETEXT(text))

	part = MIMEBase('application', 'octet-stream')
	part.set_payload(open(attach, 'rb').read())
	Encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; file=%s' %(attachment))
	msg.attach(part)

	EMAIL_HOST_SERVER.ehlo()
	EMAIL_HOST_SERVER.starttls()
	EMAIL_HOST_SERVER.ehlo()
	EMAIL_HOST_SERVER.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
	EMAIL_HOST_SERVER.sendmail(EMAIL_HOST_USER, to, msg.as_string())
	EMAIL_HOST_SERVER.close()