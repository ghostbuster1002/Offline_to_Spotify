import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth=token,client_credentials_manager=SpotifyClientCredentials())
#requires Client ID and Secret as arguments or passed as Evironement Variables

trackname="California Dreamin'"
artist= "The Mamas & The Papas"
album='If You Can Believe Your Eyes & Ears'
query=trackname+' artist:'+artist+' album:'+album
results = sp.search(query,type='track')
print(results['tracks']['items'][0]['uri'])
