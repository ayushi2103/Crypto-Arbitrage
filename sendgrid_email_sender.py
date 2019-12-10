import urllib.request as urllib
import base64
import json
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)


def send_email(email_to):
    message = Mail(
        from_email = 'dev@fidelityhackathon.com',
        to_emails = email_to,
        subject='Crypto Investment CSV File',
        html_content='<strong>Here is the file you requested.</strong>')

    file_path = os.path.join(os.getcwd(), "trades.csv")
    with open(file_path, 'rb') as f:
        data = f.read()
        f.close()
        
    encoded = base64.b64encode(data).decode()
    attachment = Attachment()
    attachment.file_content = FileContent(encoded)
    attachment.file_type = FileType('application/csv')
    attachment.file_name = FileName('trades.csv')
    attachment.disposition = Disposition('attachment')
    attachment.content_id = ContentId('Example Content ID')
    message.attachment = attachment
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return response.status_code
    except Exception as e:
        print(e.message)

if __name__ == "__main__":
    send_email("alishahimtiaz97@gmail.com")