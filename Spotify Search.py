import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
trackname="You Owe Me"
artist= "The Chainsmokers"
album=''
query=trackname+' artist:'+artist
results = sp.search(query,type='track')
print(results['tracks']['items'][0]['uri'])