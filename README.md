# startup_email
A simple raspberry PI script to help you send the ip address od raspberry pi on startup when running in headless mode. After checking out the code from GIT set a cron job to run at startup by doing crontab -e and entering the below

@reboot /usr/bin/python /home/pi/startup_email/ip_email.py to_email_addresss from_email_address from_email_password >> location_of_log_files_if_needed 2>&1 &
