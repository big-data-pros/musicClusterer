import base64
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')
load_dotenv(env_path)

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def get_spotify_token(client_id, client_secret):
    if not client_id or not client_secret:
        raise ValueError("CLIENT_ID and CLIENT_SECRET must be set in .env file")
    
    auth_str = f"{client_id}:{client_secret}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={"grant_type": "client_credentials"},
        headers={"Authorization": f"Basic {b64_auth_str}"}
    )
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        raise Exception(f"Failed to get access token: {response.text}")
    
    try:
        return response.json()["access_token"]
    except KeyError:
        print(f"Response JSON: {response.json()}")
        raise Exception("No access_token in response")

