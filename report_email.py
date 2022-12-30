#!/usr/bin/env python3
import reports
import emails
import datetime
import os


def get_title():
    date = datetime.date.today()
    return "Processed Update on {}".format(date.strftime("%B %d, %Y"))


def get_paragraph():
    source = "supplier-data/descriptions"
    result = "<br/>"
    for file in os.listdir(source):
        with open(os.path.join(source, file)) as f:
            x = f.readlines()
            name = x[0].strip()
            weight = x[1].strip()
            result += "name: {}<br/>weight: {}<br/><br/>".format(name, weight)
    return result


if __name__ == "__main__":
    # generate report
    attachment = 'tmp/processed.pdf'
    title = get_title()
    paragraph = get_paragraph()
    reports.generate_report(attachment, title, paragraph)

    # send email
    sender = "automation@example.com"
    recipient = "username@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(message)
