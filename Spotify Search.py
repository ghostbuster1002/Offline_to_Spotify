import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import AppCredentials as cred

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=cred.client_id,
                                                                         client_secret=cred.client_secret))
results = sp.search(q='weezer',limit=2)

for i,track in enumerate(results['tracks']['items']):
    t=track['id']