from fastapi import FastAPI
from google_apis import create_service

client_secret_file = 'secrets/client_secret.json'
API_SERVICE_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
service = create_service(client_secret_file, API_SERVICE_NAME, API_VERSION, SCOPES)

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
