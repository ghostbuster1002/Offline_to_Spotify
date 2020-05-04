from tinytag import TinyTag
import os

track_list=[]
track_info=['title','artist','album']
track_data=dict.fromkeys(track_info)
for subdir, dirs, files in os.walk(r'F:\New_Music'):
    for filename in files:
        if filename.endswith((".m4a",".mp3")):
            tag=TinyTag.get(subdir + os.sep + filename)
            for x in track_info:
                track_data[x]=getattr(tag,x)
            track_list.append(track_data.copy())

# tag = TinyTag.get("F:\English Music\The Feeling Is All Gone (Acoustic) - Solar Sun.mp3")
# print(tag.title,'-',tag.artist,tag.album)

