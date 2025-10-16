from dotenv import load_dotenv
import os
from fastapi import FastAPI
from gmail_api import init_gmail_service, get_email_messages, get_email_message_details, search_emails, search_email_conversations

load_dotenv()

client_secret_file = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
service = init_gmail_service(client_secret_file)

##messages = get_email_messages(service, max_results=5)
query = 'from:LinkedIn'
email_messages = search_emails(service,query,max_results=5)

for msg in email_messages:
    details = get_email_message_details(service, msg['id'])
    if details:
        print(f"Subject: {details['subject']}")
        print(f"From: {details['sender']}")
        print(f"Recipients: {details['recipients']}")
        print(f"Body: {details['body'][:100]}...")
        print(f"Snippet: {details['snippet']}")
        print(f"Has Attachments: {details['has_attachments']}")
        print(f"Date: {details['date']}")
        print(f"Star: {details['star']}")
        print(f"Label: {details['label']}")
        print("-" * 50)

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
