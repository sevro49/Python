import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "sevro4949@gmail.com"

mesaj["To"] = "sevro4949@gmail.com"

mesaj["Subject"] = "Smtp mail gönderme"

yazi = """

Smtp ile mail gönderiyorum

-Emre Güler

"""

mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()

    mail.starttls()

    mail.login("","") #gmail, password

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail başarıla gönderildi")

    mail.close()

except:
    sys.stderr.write("Bir sorun oluştu")
    sys.stderr.flush()
