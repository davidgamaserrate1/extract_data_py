import cx_Oracle
import pandas as pd
import smtplib
import zipfile
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
dsn = os.getenv("DSN") 

connection = cx_Oracle.connect(username, password, dsn)

#YOUR ORACLE QUERY WHERE
query = """

"""

df = pd.read_sql(query, con=connection)

connection.close()

output_file = "your_file.xlsx"
df.to_excel(output_file, index=False)

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_TO = 'contato.davidserrate@gmail.com'

zip_filename = "your_file.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.write(output_file)
    
os.remove(output_file)

msg = EmailMessage()
msg['Subject'] = 'Relatório - Arquivo ZIP'
msg['From'] = EMAIL_HOST_USER
msg['To'] = EMAIL_TO
msg.set_content("Olá,\n\nSegue em anexo o relatório em formato ZIP.\n\nAtenciosamente")

with open(zip_filename, 'rb') as f:
    file_data = f.read()
    msg.add_attachment(file_data, maintype='application', subtype='zip', filename=zip_filename)

with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as smtp:
    smtp.starttls()
    smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    smtp.send_message(msg)

print(f"Arquivo ZIP '{zip_filename}' gerado e enviado com sucesso!")