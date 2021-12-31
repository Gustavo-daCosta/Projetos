import os
import smtplib
from email.message import EmailMessage
from segredos import senha, email

#Configurar email e senha
EMAIL_ADDRESS = email
EMAIL_PASSWORD = senha

# Criar um email
msg = EmailMessage()
msg['Subject'] = 'Carga #35 chegou ao porto.'
msg['From'] = email
msg['To'] = 'guti.ps.hzd@gmail.com'
msg.set_content('Favor buscar a carga 35 que acaba de chegar na portaria')

# Enviar um email
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print('E-mail enviado!')
except:
    print('Ocorreu um erro e o e-mail não pode ser enviado.')