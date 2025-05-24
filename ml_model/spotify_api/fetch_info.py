import base64
import requests
import os
import sys
from dotenv import load_dotenv

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(project_root)

from ml_model.spotify_api.auth import get_spotify_token

# Load environment variables from .env file
env_path = os.path.join(project_root, '.env')
load_dotenv(env_path)

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


token = get_spotify_token(CLIENT_ID, CLIENT_SECRET)
print("Successfully obtained Spotify access token")


def search_track(track_name, token):
    headers = {"Authorization": f"Bearer {token}"}
    query = f"{track_name} "
    url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=1"
    response = requests.get(url, headers=headers)
    results = response.json()
    print(f"Search URL: {url}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response JSON: {results}")
    if results["tracks"]["items"]:
        return results["tracks"]["items"][0]
    return None

# Example:
sample = search_track("basra7 wa atooh", token)
sample["album"]["release_date"] if sample else "Not found"
