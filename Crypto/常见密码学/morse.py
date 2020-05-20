#摩斯密码加解密

def getMorse(str):#将０１的串转换成摩斯编码，结果有两种，所以函数返回一个数组，[0][1]
    str_Len = len(str)
    decodeStr1 = ''
    decodeStr2 = ''
    for i in range(str_Len):
        if str[i] == '1':
            #if str = "11 111 010 000 0 1010 111 100 0 00 000 000 111 00 10 1 0 010 0 000 1 00 10 110"
            decodeStr1 += '-'
            decodeStr2 += '.'
        elif str[i] == '0':
            decodeStr1 += '.'
            decodeStr2 += '-'
        else:
            decodeStr1 += str[i]
            decodeStr2 += str[i]
    returnStr = decodeStr1+'*'+decodeStr2
    returnStr = returnStr.split('*')
    return returnStr # return a array,you can also modify
def morse(string, sign):#摩斯解密，string为加密的编码串，sign默认为' '
    MorseList = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
        "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
        "---": "O", ".--．": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",

        "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
        ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

        ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
        "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
        "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
        "....": "&", ".--.-.": "@", ".-.-.": "+",
    }
    # 分割，字符串string，分割标识符sign
    lists = string.split(sign) # produce a array.
    for code in lists:
        print(MorseList.get(code),end='')




#str = "11 111 010 000 0 1010 111 100 0 00 000 000 111 00 10 1 0 010 0 000 1 00 10 110"
#getMorseStr=getMorse(str)
#decodeStr1 = getMorseStr[0]
#decodeStr2 = getMorseStr[1]

#morse(decodeStr1,' ')
#print("")
#morse(decodeStr2,' ')
#print()
#print("MORSECODEISSOINTERESTING".lower())
