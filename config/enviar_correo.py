from email.mime.text import MIMEText
import smtplib
# MIME = MultiPurpose Internet Mail Extensions
from email.mime.multipart import MIMEMultipart
from os import environ
from dotenv import load_dotenv
load_dotenv()

print(environ.get('EMAIL'))
mensaje = MIMEMultipart()
mensaje['From'] = environ.get('EMAIL')
mensaje['Subject'] = 'Solicitud de restauracion de la contraseña'
password = environ.get('EMAIL_PASSWORD')
print(password)


def enviarCorreo(destinatario, cuerpo):
    '''Funcion que sirve para enviar un correo'''
    mensaje['To'] = destinatario
    texto = cuerpo
    # Luego de definir el cuerpo del correo agregamos al mensaje mediante su metodo attach y en formato MIMEText en el cual recibira un texto y luego el format a convertir, si quieres enviar un html entonces pondremos en 'html', si queremos enviar un texto 'plain
    mensaje.attach(MIMEText(texto, 'plain'))
    try:
        # configurar el servidor SMTP
        servidorSMTP = smtplib.SMTP('smtp.gmail.com', 587)
        # indico el protocolo de transferencia
        servidorSMTP.starttls()
        # inicio sesion en el servidor de correos con las credenciales asignadas previamente
        servidorSMTP.login(user=mensaje.get('From'), password=password)
        servidorSMTP.sendmail(
            from_addr=mensaje.get('From'),
            to_addrs=mensaje.get('To'),
            msg=mensaje.as_string()
        )
        # cerrar la sesion de mi correo
        servidorSMTP.quit()
    except Exception as e:
        print(e)
