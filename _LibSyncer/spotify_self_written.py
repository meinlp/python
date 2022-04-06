from os import environ as env
from dotenv import load_dotenv, find_dotenv
import constants
import spotipy
from spotipy.oauth2 import SpotifyOAuth

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

SPOTIPY_CLIENT_ID = env.get(constants.SPOTIPY_CLIENT_ID, '')
SPOTIPY_CLIENT_SECRET = env.get(constants.SPOTIPY_CLIENT_SECRET, '')
SPOTIPY_REDIRECT_URI = env.get(constants.SPOTIPY_REDIRECT_URI, '')

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def get_saved_tracks():
    saved_tracks = {}
    keep_rolling = True
    offset = 0
    while keep_rolling:
        results = sp.current_user_saved_tracks(offset=offset)
        for idx, item in enumerate(results['items']):
            track = item['track']
            saved_tracks[track['artists'][0]['name']] = track['name']
            print(idx, track['artists'][0]['name'], " – ", track['name'])
        offset += 20
        if not results['next']:
            keep_rolling = False
    return saved_tracks


def get_playlists():
    pass

