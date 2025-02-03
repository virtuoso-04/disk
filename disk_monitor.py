import os
import shutil
import smtplib
from datetime import datetime
import time

# Configuration
THRESHOLD = 80  # Disk usage percentage to trigger alert
LOG_FILE = "disk_usage.log"  # Path to the log file
CHECK_INTERVAL = 60 * 5  # Time between checks in seconds (e.g., 5 minutes)

def check_disk_usage():
    total, used, free = shutil.disk_usage("/")
    percent_used = (used / total) * 100
    return total, used, free, percent_used;

def log_usage(total, used, free, percent_used):
    with open("disk_usage.csv", "a") as log:
        if log.tell() == 0:  # Write headers if file is new
            log.write("Datetime,Total,Used,Free,Usage\n")
        log.write(f"{datetime.now()},{total},{used},{free},{percent_used:.2f}\n")
def send_alert(percent_used):
    if percent_used >= THRESHOLD:
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login("anant.sharma9652knp@gmail.com", "password")
            message = f"Subject: Disk Usage Alert\n\nDisk usage is at {percent_used:.2f}%!"
            server.sendmail("anant.sharma9652knp@gmail.com", "anantsharma0408@gmail.com", message)

def monitor_disk():
    total, used, free, percent_used = check_disk_usage()
    log_usage(total, used, free, percent_used)
    if percent_used >= THRESHOLD:
        send_alert(percent_used)

if __name__ == "__main__":
    monitor_disk()

