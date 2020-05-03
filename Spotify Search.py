import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
trackname="California Dreamin'"
artist= "The Mamas & The Papas"
album='If You Can Believe Your Eyes & Ears'
query=trackname+' artist:'+artist+' album:'+album
results = sp.search(query,type='track')
print(results['tracks']['items'][0]['uri'])