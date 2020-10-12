# base64加解密
def base(string:str)->str:#base64加密
    base64_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c','d','e','f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
#把原始字符串转换为二进制，用bin转换后是0b开头的，所以把b替换了，首位补0补齐8位
    for i in range(14):
        base = ''
        oldstr = ''
        newstr = []
        base64_rec=','.join(base64_list)
        base64_list=(base64_rec,i).split(',')
        for i in string:
            oldstr += '{:08}'.format(int(str(bin(ord(i))).replace('0b', '')))
#把转换好的二进制按照6位一组分好，最后一组不足6位的后面补0
        for j in range(0, len(oldstr), 6):
            newstr.append('{:<06}'.format(oldstr[j:j + 6]))
#在base_list中找到对应的字符，拼接

        for l in range(len(newstr)):
            base += base64_list[int(newstr[l], 2)]
    #判断base字符结尾补几个‘=’
        if len(string) % 3 == 1:
            base += '=='
        elif len(string) % 3 == 2:
            base += '='
        print(base)
        #print("key="+i+"  decode:"+debase(base))
def debase(string:str)->str:#base64解密
    base64_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 
                    'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                    's', 't', 'u', 'v','w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
    for i in range(14):
        base64_rec=','.join(base64_list)
        base64_list=(base64_rec,i).split(',')
        oldstr=''
        unbase=''
        for i in string.replace('=',''):
            oldstr += '{:06}'.format(int(bin(base64_list.index(i)).replace('0b', '')))
        newstr = ['{}'.format(oldstr[j:j + 8]) for j in range(0, len(oldstr), 8)]
        for l in range(len(newstr)):
            unbase += chr(int(newstr[l], 2))
        print(unbase)

import base64
str = "19aaFYsQQKr+hVX6hl2smAUQ5a767TsULEUebWSajEo="
print(base64.b64decode(str.encode('utf-8')))