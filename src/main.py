from dotenv import load_dotenv
import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv("C:\\Users\\Vivupadi\\Desktop\\Music_recommender\\src\Auth.env")

SPOTIFY_CLIENT_ID = os.getenv('client_id')
SPOTIFY_CLIENT_SECRET = os.getenv('client_secret')
SPOTIFY_REDIRECT_URI = 'http://localhost:8888/callback'

#breakpoint()
sp =  spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-top-read"
))

# Fetch top artists for the authenticated user
top_artists = sp.current_user_top_artists(limit=10)  # Get top 10 artists (you can change the limit)

# Print the names of the top artists
for idx, artist in enumerate(top_artists['items']):
    print(f"{idx + 1}: {artist['name']}")