import smtplib
from email.message import EmailMessage
import os
 
FROM_EMAIL = os.environ.get("EMAIL_USERNAME")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")
 
msg = EmailMessage()
msg['Subject'] = 'CAST AI Automation Report'
msg['From'] = FROM_EMAIL
msg['To'] = TO_EMAIL
 
msg.set_content("Hello,\n\nPlease find attached the latest CAST AI reports.\n\nThanks,\nCASTAI-Report Pipeline")
 
# Attach merged Excel
excel_path = "cast.ai_report/merged_output.xlsx"
 
if os.path.exists(excel_path):
    with open(excel_path, 'rb') as f:
        msg.add_attachment(
            f.read(),
            maintype='application',
            subtype='octet-stream',
            filename='merged_output.xlsx'
        )
 
# Attach HTML report
html_path = "cast.ai_report/report.html"
 
if os.path.exists(html_path):
    with open(html_path, 'rb') as f:
        msg.add_attachment(
            f.read(),
            maintype='text',
            subtype='html',
            filename='report.html'
        )
 
# Send Email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(FROM_EMAIL, EMAIL_PASSWORD)
    smtp.send_message(msg)
 
print("Email sent successfully!")
 