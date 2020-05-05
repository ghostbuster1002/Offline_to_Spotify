import os
import spotipy
from tinytag import TinyTag
sp = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())

def query(track):
    q = track['title'] + ' artist:' + track['artist']
    if (track['album']):
        q+= ' album:' + track['album']
    return q

def urisearch(track):
    sresult = sp.search(query(track), type='track', limit=1)
    if sresult['tracks']['items']:
        track['uri'] = sresult['tracks']['items'][0]['uri']
        return [track,True]
    else:
        return [track,False]

def searchbyfilename(track,filename):
    name=filename.split(' - ')
    track['title']=name[0]
    track['artist']=os.path.splitext(name[1])[0]
    track['album']=''
    return urisearch(track)

def gettracks(path):
    track_info=['title','artist','album','uri']
    track_data=dict.fromkeys(track_info)
    track_list=[]
    found=False
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith((".m4a",".mp3")):
                tag=TinyTag.get(subdir + os.sep + filename)
                for x in track_info:
                    if x is 'uri':
                        while found is False:
                            [track_data,found]=urisearch(track_data) #Search by ID3Tag
                            if found is not True:     #Try one more time with filename
                                [track_data,found]=searchbyfilename(track_data,filename)
                                if track_data['album']=='' and found is False:
                                    break
                                else:
                                    track_data['album']=''
                    else:
                        track_data[x]=getattr(tag,x) #Get ID3 data
                track_list.append(track_data.copy())
    return track_list

path=r'F:\New_Music'
tracks=gettracks(path)
for track in tracks:
    print(track['title'],'-',track['artist'],' (',track['album'],') ',track['uri'])