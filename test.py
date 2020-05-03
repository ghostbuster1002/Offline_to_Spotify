import urllib.parse as p #For Parsing the Track Name with
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='01e4ef84a877453e8b4f711e15ee4951',
                                                      client_secret='2faaaf0f2f3d4a0584540d889d735c19')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
username='kapilkalra'
scope='user-modify-playback-state playlist-modify-private user-read-private'
token=util.prompt_for_user_token(username, scope,
                           client_id='01e4ef84a877453e8b4f711e15ee4951',
                           client_secret='2faaaf0f2f3d4a0584540d889d735c19',
                           redirect_uri='http://localhost:80')
sp=spotipy.client.Spotify(auth=token)
print(token)
trackname = 'Get Lucky'
artistname= 'Daft Punk'
albumname= 'Random Access Memories'
query='track:'+trackname+' artist:'+artistname+' album:'+albumname
q=p.quote(query,safe=':')
print(q)
sp.set_auth(token)
s_result=sp.search(q,type='track')
print(s_result)
sp.add_to_queue('spotify:track:0dEIca2nhcxDUV8C5QkPYb', device_id=None)
# TODO: Remember to add field filters to query.
#https://developer.spotify.com/documentation/web-api/reference/search/search/
#https://spotipy.readthedocs.io/en/2.12.0/#examples