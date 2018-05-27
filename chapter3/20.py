import json

with open('jawiki-country.json') as jfile:
    jline = jfile.readline()
    while jline:
        jdict = json.loads(jline)
        if jdict['title'] == 'イギリス':
            print(jdict['text'])
        jline = jfile.readline()
