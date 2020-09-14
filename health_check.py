#!/usr/bin/env python3

import shutil, psutil, os, sys, socket
from emails import generate_alert_email, send_email

def check_cpu_constrained():
    """Returns True if there is >20% CPU available, False otherwise"""
    cpu_percent = psutil.cpu_percent(1)
    if cpu_percent > 20:
        return False
    return True

def check_disk_storage():
    """Returns True if there is enough free disk space, False otherwise"""
    du = shutil.disk_usage('/')
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    if percent_free < 20:
        return False
    return True

def check_available_RAM():
    """Returns True if available RAM > 500MB, false otherwise"""
    available_RAM = psutil.virtual_memory().available / 1000000
    if available_RAM < 500:
        return False
    return True

def check_host():
    """Returns True if 'localhost' is resolved to "127.0.0.1", False otherwise"""
    if socket.gethostbyname('localhost') != '127.0.0.1':
        return False
    return True

def main():
    checks = [
    (check_cpu_constrained, 'Error - CPU usage is over 80%'),
    (check_disk_storage, 'Error - Available disk space is less than 20%'),
    (check_available_RAM, 'Error - Available memory is less than 500MB'),
    (check_host, 'Error - localhost cannot be resolved to 127.0.0.1'),
    ]
    everything_ok = True
    for checkIsGood, msg in checks:
        if checkIsGood is False:
            email = generate_alert_email(
            sender='automation@example.com',
            recipient='student-01-d177668c7ce9@example.com', #UPDATE WITH LAB CREDENTIALS@example.com
            subject=msg,
            body='Please check your system and resolve the issue as soon as possible.')
            send_email(email)
            print("Alert sent successfully")
            everything_ok = False
    if not everything_ok:
        sys.exit(1)
    else:
        print("Everything ok.")
        sys.exit(0)

main()
