# rot13解密
import sys
# rot = sys.argv[1]
def rot13(rot,j):
    c=""
    for i in rot:
        if ord(i)-97>=0 and ord(i)-97<=25:
            if ord(i)-97<=12:
                a=ord(i)
                a=a+j
                c=c+chr(a)
            else:
                a=ord(i)
                a=a-j
                c=c+chr(a)
            continue
        if (ord(i)-65>=0 and ord(i)-65<=25):
            if ord(i)-65<=12:
                a=ord(i)
                a=a+j
                c=c+chr(a)
            else:
                a=ord(i)
                a=a-j
                c=c+chr(a)
            continue
        else:
            c=c+i
    return c
rot = ":D@J::K=r<ecXi^\[V:X\jXit"

# b = rot13(rot)
for i in range(14):
    print(rot13(rot,i))
print(b)

