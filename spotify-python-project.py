import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import time

from pprint import pprint

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
access_token = config.access_token

cid = config.ClientID
secret = config.ClientSecret
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)


#ID for Simon & Garfunkel - https://open.spotify.com/artist/70cRZdQywnSFp9pnc2WTCE?si=vLHMSEoAR-WXVDT4O1a9Sw&nd=1
#urn = 'spotify:artist:70cRZdQywnSFp9pnc2WTCE'

#artist = sp.artist(urn)
#print(artist)

#user = sp.user('plamere')
#print(user)



def get_current_track(access_token):
    print("test")
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()
    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]
    print("test2")
    link = json_resp['item']['external_urls']['spotify']

    artist_names = ', '.join([artist['name'] for artist in artists])

    current_track_info = {
    	"id": track_id,
    	"track_name": track_name,
    	"artists": artist_names,
    	"link": link
    }
    print("test3")
    pprint(
		    	current_track_info,
		    	indent=4,
		    )
    return current_track_info


get_current_track(access_token)

                             



#To-Do

#Stats from Artits

#Get Profile picture URL

#Start displaying on webpage

#Display data in bar charts and pie charts