<p>This script is just a challenge for me to create something from scratch using only Python</p>
<p>It uses some libs listed below:</p>
<ul>
    <li>Pynput - to capture what is being digited</li>
    <li>Datetime - to check the last date that the script has sent the log file and compare it with the current date</li>
    <li>Linecache - to get any line from a text file</li>
    <li>Smtplib - to send the email</li>
    <li>Pyautogui - to get the active window name</li>
    <li>And Sys - to increase the recursion limit of the script</li>
</ul>
<p>It's importante to note that this script uses Pyinstaller to compile the software allowing him to run on Windows as a .EXE file</p>
<h2>How to use</h2>
<p>First, you need to check if you have all the libs and dependencies installed using pip.</p>
<p>Change the necessary time to send the log in line 28. The default is 7 days, if it pass that stipulated time then the script will send the email and restart the log file.</p>
<p>Then you can start changing "check_file" and "log_file" to something like:</p>
<ul>
    <li>check.dll and log.dll</li>
    <li>config.ini and data.log</li>
    <li>If you wanna hide your files, then at least change their names</li>
</ul>
<p>With that, we can generate the credentials for the SMTP server using Google Gmail</p>
<p>Keep in mind that Google SMTP server only works if you have the 2-Step Verification enabled and a generated password for your app. You can use other SMTP servers to send the log to your email, but in this casez we will use Google SMTP</p>
<p>In order to do that you will need to:</p>
<ol>
    <li>Enable 2-Step Verification in Security</li>
    <img src="readme_images/Tutorial1.png" alt="">
    <li>Generate a password under the option App passwords, with the name of your application. For example, you can put Python or something like that</li>
    <img src="readme_images/Tutorial2.png" alt="">
    <img src="readme_images/Tutorial3.png" alt="">
    <li>Grab that password and put it with your email in the script</li>
</ol>
<p>Finally, whe can compile our script using Pyinstaller with:</p>
<code style="background-color: rgb(53, 53, 53); color: aliceblue;"> pyinstaller -w --onefile --icon=app.ico Key.py </code>
<p>It will generate a .EXE file that can be saved in any folder with the check and log files with it</p>
<p>In order for the program to work at Windows startup, it's important to create a link under <code style="background-color: rgb(53, 53, 53); color: aliceblue;"> C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup</code> for admin users and <code style="background-color: rgb(53, 53, 53); color: aliceblue;">C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup</code> for non-admin users</p>
<h2>Last words</h2>
<p>You can easily check that this program isn't that secure. There's no check if the necessary files exist or ways to hide your email and password if someone decompiles your program.</p>
<p>Using a function under the same function creates a recursion in the script, and that can lead to memory overflow. As you can see, this occurs on line 146, so I increased the limit of a possible recursion, since when the computer restarts, the script's memory is cleaned.</p>
<p>THIS PROJECT IS FOR EDUCATIONAL PURPOSES ONLY, SO DO NOT TRY TO HARM PEOPLE USING IT</p>
