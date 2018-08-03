import json


with open("jawiki-country.json", "r") as file:
    line = file.readline() 
    while line:
        json_dict = json.loads(line)
        if json_dict['title'] == 'イギリス':
            print(json_dict['text'])
        line = file.readline()
