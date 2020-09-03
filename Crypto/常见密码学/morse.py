#字符串转换成摩斯编码，结果有两种，所以函数返回一个数组，[0][1]
def To_Morse(str):
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

str1 = '.-.-..-..--....-.---..-...-....-...--.-......---........--..-----..-.....---..--....................'
# str = '.. .-.. --- ...- . -.-- --- ..-'
str2 = ''
for i in str1:
    if i=='.':
        str2+='0'
    else:
        str2+='1'

print(str2)

str_test="01001101100101100001010110111100010000110001111110000001111110000000101001"
str2 = '01010010011000010111001000100001000110100000011100000000110011111001000001110011000000000000000000001101'
str3 = '0101101100111000101111111000100110001111110000'
import re
# a = re.findall(r'.{7}',str2)
b = re.findall(r'.{8}',str2)
# for i in a:
    # print(chr(int(i,2)),end='')
# print('')
# for i in b:
#     print(chr(int(i, 2)),end='')
# print('')
for i in b:
    print(hex(int(i, 2)), end='')

    #... -... -.-. ----. ..--- ..... -.... ....- ----. -.-. -... ----- .---- ---.. ---.. ..-. ..... ..--- . -.... .---- --... -.. --... ----- ----. ..--- ----. .---- ----. .---- -.-."
# morse(str1,' ')
# morse(str2,' ')
#str = "11 111 010 000 0 1010 111 100 0 00 000 000 111 00 10 1 0 010 0 000 1 00 10 110"
#getMorseStr=getMorse(str)
#decodeStr1 = getMorseStr[0]
#decodeStr2 = getMorseStr[1]

#morse(decodeStr1,' ')
#print("")
#morse(decodeStr2,' ')
#print()
#print("MORSECODEISSOINTERESTING".lower())
