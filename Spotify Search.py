import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
trackname="California Dreamin'"
artist= "The Mamas & The Papas"
album=''
query=trackname+' artist:'+artist
results = sp.search(query,type='track')
try:
    url=results['tracks']['items'][0]['uri']
except:
    print('it throws error')
else:
    print('it doesn\'t throw an error',url)
