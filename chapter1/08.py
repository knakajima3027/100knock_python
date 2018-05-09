centence = 'Can you speak Japanese'
print(centence) #暗号化する文書
def cipher(target):
    result_list = []
    result = ''
    for i in range(len(target)):
        if target[i].islower():
            result_list.append(chr(219 - ord(target[i])))
        else:
            result_list.append(target[i])

    for i in range(len(result_list)):
        result += result_list[i]

    return result

encryption = cipher(centence)
print(encryption) #文字列の暗号化

decryption = cipher(encryption)
print(decryption) #文字列の復号化
