import json

def pick_UK(): 
    text = ''
    with open("jawiki-country.json", "r") as f:
        json_file = f.readline() #jsonファイルを一行だけ読み込む

        while json_file: #最後の行を読み込むまで繰り返し
            json_dict = json.loads(json_file) #jsonファイルを辞書型に変換

            if json_dict['title'] == 'イギリス':
                text += json_dict['text']

            json_file = f.readline()  
    
    return text
            
if __name__ == '__main__':
    print(pick_UK())
