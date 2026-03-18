import requests
import os
 
webhook_url = os.environ.get("TEAMS_WEBHOOK_URL")
 
message = {
    "text": "CAST AI Automation Pipeline Completed Successfully!\n\n Reports Generated:\n- Merged Excel\n- HTML Dashboard\n\n📁 Check GitHub Actions artifacts for full details."
}
 
response = requests.post(webhook_url, json=message)
 
if response.status_code == 200:
    print("Message sent to Teams successfully!")
else:
    print(f"Failed to send message: {response.status_code}")
 