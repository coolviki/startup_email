import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime
import time
import sys

# Delay the email by 60 seconds
time.sleep(30)
def connect_type(word_list):
    """ This function takes a list of words, then, depeding which key word, ret$
    internet connection type as a string. ie) 'ethernet'.
    """
    if 'wlan0' in word_list or 'wlan1' in word_list:
        con_type = 'wifi'
    elif 'eth0' in word_list:
        con_type = 'ethernet'
    else:
        con_type = 'current'


import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime
import time

# Delay the email by 60 seconds
time.sleep(30)
def connect_type(word_list):
    """ This function takes a list of words, then, depeding which key word, ret$
    internet connection type as a string. ie) 'ethernet'.
    """
    if 'wlan0' in word_list or 'wlan1' in word_list:
        con_type = 'wifi'
    elif 'eth0' in word_list:
        con_type = 'ethernet'
    else:
        con_type = 'current'
    return con_type

# Change to your own account information
if len(sys.argv) <4:
	print ("Incorrect no of args. exiting program")
	sys.exit() 
# Account Information
to = sys.argv[1] # Email to send to.
gmail_user = sys.argv[2] # Email to send from. (MUST BE GMAIL)
gmail_password = sys.argv[3] # Gmail password.
smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.

smtpserver.ehlo()  # Says 'hello' to the server
smtpserver.starttls()  # Start TLS encryption
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_password)  # Log in to server
today = datetime.date.today()  # Get current time/date

arg='ip route list'  # Linux command to retrieve ip addresses.
# Runs 'arg' in a 'hidden terminal'.
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()  # Get data from 'p terminal'.

print len(data)
print data


# Creates the text, subject, 'from', and 'to' of the message.
msg = MIMEText(''.join(data[0]))
msg['Subject'] = 'IPs For RaspberryPi 4 - The new machine' 
msg['From'] = gmail_user
msg['To'] = to

# Sends the message
smtpserver.sendmail(gmail_user, [to], msg.as_string())
# Closes the smtp server.
smtpserver.quit()

