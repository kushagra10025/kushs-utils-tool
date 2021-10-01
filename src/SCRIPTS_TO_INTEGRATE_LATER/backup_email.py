'''


Config example:
{
    "subject" : "Daily backup",
    "body" : "This is a daily database backup",
    "sender_email" : "sender@gmail.com",
    "receiver_email" : "receiver@gmail.com",
    "password" : "supersecretpassword",
    "smtp_server" : "smtp.gmail.com",
    "smtp_host" : 465,
    "dbname" : "dbname",
    "file_prefix": "dbname_backup"
}


'''

import email, smtplib, ssl
import datetime
import subprocess
import shlex
import json
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CONFIG_FILE = 'backup_email.json'

with open(CONFIG_FILE, 'r') as f:
    config = json.load(f)

subject = config['subject']
body = config['body']
sender_email = config['sender_email']
receiver_email = config['receiver_email']
password = config['password']
smtp_server = config['smtp_server']
smtp_host = config['smtp_host']
dbname = config['dbname']
file_prefix = config['file_prefix']

cmd1 = "mysqldump {}".format(dbname)
cmd2 = "gzip -9"
filename = "{}_{}.sql.gz".format(file_prefix, datetime.datetime.now().strftime('%Y%m%d%H%M'))

# Backup database
print('Backing up database..')
with open(filename, 'w') as f:
    ps1 = subprocess.Popen(shlex.split(cmd1), stdout=subprocess.PIPE)
    ps2 = subprocess.Popen(shlex.split(cmd2), stdin=ps1.stdout, stdout=f)
    ps1.wait()
    ps2.wait()
    if ps2.returncode == 2:
        exit(1)

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
print('Sending email..')
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, smtp_host, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)

print('Done.')