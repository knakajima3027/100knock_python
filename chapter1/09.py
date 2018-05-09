import random

centence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

word_list = centence.split(' ')
Ty_centence = ''



for i in range(len(word_list)):
    result = ''
    Ty_word = []
    if len(word_list[i]) > 4:
        str_list = word_list[i].split()
        Ty_word.append(str_list[0])
        a = str_list[-1]
        str_list.pop(0)
        str_list.pop(-1)
        random.shuffle(str_list[i])
        for j in range(len(str_list)):
            Ty_word.append(str_list[j])

        Ty_word.append(a)
        for j in range(len(str_list[j])):
            result += Ty_word[j]
    else:
        result = word_list[i]

    Ty_centence += result + ' '

print(Ty_centence)
