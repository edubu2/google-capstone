#!/usr/bin/env python3

from emails import generate_email, send_email
from reports import generate_report

def main():
    generate_report()
    msg = generate_email(
    sender='automation@example.com',
    recipient='student-01-d177668c7ce9@example.com', # UPDATE WITH LAB EXTERNAL IP
    subject='Upload Completed - Online Fruit Store',
    body='All fruits are uploaded to our website successfully. A detailed list is attached to this email.',
    attachment_path='/tmp/processed.pdf')
    send_email(msg)

if __name__ == '__main__':
    main()
