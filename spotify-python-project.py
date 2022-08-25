import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = config.ClientID
secret = config.ClientSecret
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)


urn = 'spotify:artist:70cRZdQywnSFp9pnc2WTCE'

artist = sp.artist(urn)
print(artist)

user = sp.user('plamere')
print(user)