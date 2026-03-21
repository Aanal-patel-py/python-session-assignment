import smtplib
from email.message import EmailMessage


mail='aanal.patel@simformsolutions.com'

msg = EmailMessage()
msg['From'] = mail
msg['To'] = 'Aom.kapadia@simformsolutions.com'
msg['Subject'] = 'Hello'
msg.set_content('This is a test email.')

with smtplib.SMTP('smtp.outlook.com',587) as smtp:
    x=smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    print(x)

    smtp.login()
    
    # subject='practicing email module'
    # body='123'

    # msg=f'Subject: {subject}\n\n{body}'
    smtp.send_message(msg)
