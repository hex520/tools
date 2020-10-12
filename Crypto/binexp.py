#! /usr/bin/env python3
import math
str1  = "8842101220480224404014224202480122"
def yunying(en_str):#云影解密
    en_str = en_str.split('0')
    a = []
    for i in en_str:

        sum = 0
        for j in i:
            sum+=int(j)
        print(chr(sum+64),end='')
        a.append(sum)
    print()
    return a


b = yunying(str1)



def binexp(arr):# 幂数解密
    for i in arr:
        sum = 0
        for j in str(i):
            sum += math.pow(2,int(j))
        print(chr(int(sum) + 64), end='')
binexp(b)

