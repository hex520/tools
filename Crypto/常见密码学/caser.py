#凯撒密码解密
str = "oknqdbqmoq{kag_tmhq_xqmdzqp_omqemd_qzodkbfuaz}"
str1 = "ccehgyaefnpeoobe{lcirg}epriec_ora_g"
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
    print(a)

