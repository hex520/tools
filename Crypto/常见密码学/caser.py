#凯撒密码解密
import sys
str1 = sys.argv[1]
def caser(str,key):#key为移位
    str_1=''
    for i in str:
        if ord(i)>=65 and ord(i)<= 90:
            str_1 +=chr((ord(i) - 65 + key) % 26 + 65)
        elif ord(i) >= 97 and ord(i) <= 122:
            str_1 += chr((ord(i) - 97 + key) % 26 + 97)
        else:
            str_1+=i
    return str_1
for i in range(26):
    a=caser(str1,i)
    print("第{}次解密:{}".format(i,a))

