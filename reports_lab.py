#!/usr/bin/env python3

import os

#update run_local to run in actual lab
from run import generate_json, descriptions
from reportlab.platypus import SimpleDocTemplate, Paragraph
#import sample style sheet to use html-like headings in the PDF file
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

def generate_report():
    data = generate_json(descriptions)
    pdf_output_location = "/tmp/processed.pdf"
    # create a report object
    report = SimpleDocTemplate(pdf_output_location)
    styles = getSampleStyleSheet()
    # format today's date into string that will be used in PDF's title
    dt = datetime.date(datetime.now())
    today = "{}/{}/{}".format(dt.month, dt.day, dt.year)
    report_title = Paragraph('Processed Update on ' + today, styles["h1"])
    # loop thru descriptions to make the body of the PDF (list of strings)
    body = ['\n']
    for desc in data:
        # add name & weight (tuple) to body list
        item_name = "name: {}".format(desc['name'])
        item_weight = "weight: {} lbs".format(str(desc['weight']))
        body.append(item_name)
        body.append(item_weight)
        body.append('\n')
    # use join to join the list into one string, separated by blank lines ('<br />')
    body_pdf = "<br />".join(body)
    report_body = Paragraph(body_pdf, styles["BodyText"])
    report.build([report_title, report_body])
