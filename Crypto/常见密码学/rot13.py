# rot13解密
def rot13(rot):
    c=""
    for i in rot:
        if ord(i)-97>=0 and ord(i)-97<=25:
            if ord(i)-97<=12:
                a=ord(i)
                a=a+13
                c=c+chr(a)
            else:
                a=ord(i)
                a=a-13
                c=c+chr(a)
            continue
        if (ord(i)-65>=0 and ord(i)-65<=25):
            if ord(i)-65<=12:
                a=ord(i)
                a=a+13
                c=c+chr(a)
            else:
                a=ord(i)
                a=a-13
                c=c+chr(a)
            continue
        else:
            c=c+i
    return c


