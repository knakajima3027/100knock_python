import sys
import MeCab

mec_text = ''
with open('neko.txt', 'r') as neko:
    m = MeCab.Tagger ("-Ochasen")
    neko_text = neko.readline()
    while neko_text:
        mec_text += m.parse(neko_text)    
        neko_text = neko.readline()
    
    with open('neko.txt.mecab', 'w') as mecab_neko:
        mecab_neko.write(mec_text)
