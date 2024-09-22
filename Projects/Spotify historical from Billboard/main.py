import os
import spotipy
import requests
from time import sleep
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

# INIT #
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URL = os.getenv("SPOTIFY_REDIRECT_URL")

auth_manager = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET,
                            redirect_uri=SPOTIFY_REDIRECT_URL,
                            scope="user-library-read,"
                                  "playlist-read-private,"
                                  "playlist-read-collaborative,"
                                  "playlist-modify-private,"
                                  "playlist-modify-public")
spotify = spotipy.Spotify(auth_manager=auth_manager)
username = spotify.me()['id']


# FUNCTIONS #
def create_song_list(date):
    soup = BeautifulSoup(requests.get("https://www.billboard.com/charts/hot-100/" + date).text, "html.parser")
    list_items = soup.find_all('li', class_='o-chart-results-list__item')
    songs = {}
    index = 1
    for item in list_items:
        try:
            artist = item.find('span', class_='c-label').get_text(strip=True)
            title = item.find('h3', id='title-of-a-story').get_text(strip=True)
            songs[index] = f'{artist}: {title}'
            index += 1
        except Exception as e:
            pass
    return songs


# I don't need this one, but just in case
def delete_all_songs_from_playlist(playlist_id):
    try:
        playlist = spotify.playlist(playlist_id)
        songs_uris = [item['track']['uri'] for item in playlist['tracks']['items']]
        while playlist['tracks']['next']:
            playlist = spotify.next(playlist['tracks'])
            songs_uris.extend([item['track']['uri'] for item in playlist['tracks']['items']])
        spotify.playlist_remove_all_occurrences_of_items(playlist_id=playlist_id, items=songs_uris)

    except Exception as e:
        print(f"An error occurred while trying to delete songs from playlist: {e}")


def create_playlist(user, identificator=None):
    result = spotify.user_playlist_create(user=user, name=f'Billboard historical {identificator}',
                                          public=True, collaborative=False,
                                          description='This playlist was created with python script. Bep-bop')
    return result['id']


def populate_playlist(playlist_id, songs):
    songs_to_add = []
    for song in songs.values():
        try:
            results = spotify.search(q=song)['tracks']['items']
            if results:
                candidate = results[0]['uri']
                songs_to_add.append(candidate)
            else:
                print(f"No results found for song: {song}")
        except Exception as e:
            print(f"An error occurred while trying to add song: {song}, Error: {e}")

        if len(songs_to_add) >= 99:
            try:
                spotify.playlist_add_items(playlist_id=playlist_id, items=songs_to_add)
                songs_to_add = []
            except Exception as e:
                print(f"Failed to add songs to playlist: {e}")
        sleep(0.01)

    if songs_to_add:
        try:
            spotify.playlist_add_items(playlist_id=playlist_id, items=songs_to_add)
        except Exception as e:
            print(f"Failed to add remaining songs to playlist: {e}")


# LOGIC
if __name__ == '__main__':
    desired_date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD\n")
    # desired_date = '1986-01-31'
    song_list = create_song_list(desired_date)
    playlist_id = create_playlist(user=username, identificator=desired_date)
    populate_playlist(playlist_id=playlist_id, songs=song_list)
