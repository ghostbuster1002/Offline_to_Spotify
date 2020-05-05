import os
import spotipy
from tinytag import TinyTag

def gettracks(path):
    track_list = []
    track_info = ['title', 'artist', 'album']
    track_data = dict.fromkeys(track_info)
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith((".m4a", ".mp3")):
                tag = TinyTag.get(subdir + os.sep + filename)
                for x in track_info:
                    track_data[x] = getattr(tag, x)
                track_list.append(track_data.copy())
    return track_list


def spotifysearch(track_list):
    sp = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())
    failed_tracks = []
    uri_list = []
    for track in track_list:
        query = track['title'] + ' artist:' + track['artist']
        if (track['album']):
            query += ' album:' + track['album']
        sresults = sp.search(query, type='track', limit=1)
        try:
            uri = sresults['tracks']['items'][0]['uri']
        except:
            failed_tracks.append(track)
        else:
            uri_list.append(uri)
    results = {
        "successful": uri_list,
        "failed": failed_tracks
    }
    return results


path = r'F:\New_Music'
tracks = gettracks(path)
results = spotifysearch(tracks)
print('URI found:',results['successful'])