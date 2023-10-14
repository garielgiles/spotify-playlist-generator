import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv


load_dotenv()

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
client_username = os.getenv('YOUR_USERNAME')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id,
    client_secret,
    redirect_uri,
    scope='playlist-modify-public'))

playlist_name = "Fresh Playlist"
playlist_description = "Testing out this music playlist generator"
playlist_id = sp.user_playlist_create(user=client_username,
                                      name=playlist_name,
                                      public=True,
                                      description=playlist_description)['id']

random_tracks = sp.search(q='genre:metal',
                          type='track',
                          limit=30)
track_ids = [track['id'] for track in random_tracks['tracks']['items']]

sp.playlist_add_items(playlist_id, items=track_ids)

names = sp.playlist_items(playlist_id='17FdPmjhtzfjgbJYTYyBsi', fields='items(track(name))')
print(f'Playlist created with 30 random tracks listed as follows: "+ {names}" ')
