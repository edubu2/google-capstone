#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate_email(sender, recipient, subject, body, *attachment_path):
    """Creates an email with an attachement."""
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)
    # if there's an attachment, process it & add it to the message
    # the for-loop is needed in order for this function to support emails w/o attachments
    for attachment in attachment_path:
        # process the attachment w/ it's mimetype & attach to email
        attachment_filename = os.path.basename(attachment)
        mime_type, _ = mimetypes.guess_type(attachment)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment, 'rb') as ap:
            message.add_attachment(ap.read(),
            maintype=mime_type,
            subtype=mime_subtype,
            filename=attachment_filename)
    return message

def send_email(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()