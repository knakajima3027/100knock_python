import plyvel

artist_db = plyvel.DB('./artists.ldb', create_if_missing=True)
count = 0

for key, value in artist_db:
    if value.decode('utf-8') == 'Japan':
        count += 1
        
print(count)
