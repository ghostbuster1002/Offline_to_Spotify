import spotipy

username = 'kapilkalra'
scopes = 'playlist-modify-private user-read-private'
token = spotipy.util.prompt_for_user_token(username, scopes)
sp = spotipy.Spotify(auth=token,client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())
playlist = sp.user_playlist_create(username, 'playlist create test1', public=False, description='Test1')
tracks=["spotify:track:5kLCPJTwcrin5Ei8AbbvdZ","spotify:track:7CoMBpPTwQi2wPT0U0Nr9b"]
sp.user_playlist_add_tracks(username,playlist.get('id'),tracks)