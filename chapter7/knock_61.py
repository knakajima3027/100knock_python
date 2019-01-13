import plyvel

artist_name = input()
artist_db = plyvel.DB('./artists.ldb', create_if_missing=True)
artist_area = artist_db.get(artist_name.encode('utf-8'))
print(artist_area.decode('utf-8'))
