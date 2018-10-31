from pprint import pprint 

map_list = []
with open('neko.txt.mecab') as mec_text:
    text = mec_text.readline()
    while text:
        text = text.split('\t')
        dic = {}
        if text[0] == 'EOS\n':
            pass
        else:
            hinshi = text[3].split('-')
            dic['surface'] = text[0]
            dic['base'] = text[2]
            dic['pos'] = hinshi[0]
            
            if ('-' in text[3]):
                dic['pos1'] = hinshi[1]
            else:
                dic['pos1'] = '*'
        
            map_list.append(dic)
            
        text = mec_text.readline()


for i in range(len(map_list)):
    tmp = ''
    flag = 0
    if map_list[i]['pos'] == '名詞':
        j = 1
        tmp = map_list[i]['surface']
        while(True):
            if map_list[i+j]['pos'] == '名詞':
                flag = 1
                tmp +=  map_list[i+j]['surface']
            else:
                break            
            j += 1
    if flag == 1:
        pprint(tmp) 
