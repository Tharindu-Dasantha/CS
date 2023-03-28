from email.message import EmailMessage 
import ssl
import smtplib 

email_sender = "cs50tharindu@gmail.com"
email_password = "kdebgekgukvnwlse"

email_receviver = 'godage5780@jthoven.com'

subject = "Hello, This is a test mail"
body = '''
I created a python automatic mail app just tring if it works.
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receviver 
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receviver, em.as_string())
    
