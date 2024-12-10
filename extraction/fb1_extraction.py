import requests
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise ValueError("Access token not found in environment variables.")

URL = "https://graph.facebook.com/v12.0/me/friends"

params = {
    "access_token": ACCESS_TOKEN
}

response = requests.get(URL, params=params)

if response.status_code == 200:
    data = response.json()
    friends = [friend["name"] for friend in data.get("data", [])]
    print(friends)
else:
    print(f"Error: {response.status_code}, {response.text}")
