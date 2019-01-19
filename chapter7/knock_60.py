import plyvel
import json
artist_db = plyvel.DB('./artists.ldb', create_if_missing=True)  # なければつくる
artist_id = 0

with open("artist.json", "r", encoding="utf-8") as jsonfile:
    for line in jsonfile:
        artist = json.loads(line)
        try:
            artist_db.put((str(artist['id']) + '\t' + artist['name']).encode('utf-8'), artist['area'].encode('utf-8'))
        except:
            artist_db.put((str(artist['id']) + '\t' + artist['name']).encode('utf-8'), 'None'.encode('utf-8'))
        
        artist_id += 1

print(artist_id)
artist_db.close()
