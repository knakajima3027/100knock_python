import requests
import json
from knock_25 import make_dict

if __name__ == '__main__':
    url = 'https://www.mediawiki.org/w/api.php'
    uk_dict = {}
    make_dict(uk_dict)
    params = {'format': 'json', 'action': 'query', 'prop': 'imageinfo', 'iiprop': 'url', 'titles': 'File:{}'.format(uk_dict['国旗画像'])}
    res = requests.get(url, params=params)
    response = res.json()
    print(response['query']['pages']['-1']['imageinfo'][0]['url'])
