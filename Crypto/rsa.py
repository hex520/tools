#! /usr/bin/env python3
import gmpy2
p = 473398607160
q = 4511491
e = 17
p1 = gmpy2.mpz(p)#初始化大整数
q1 = gmpy2.mpz(q)
e1 = gmpy2.mpz(e)
phi_n = (p1-1)*(q1-1)
d = gmpy2.invert(e1,phi_n)#invert（x，m）返回y使得x * y == 1 modulo m，如果不存在y，则返回0
print("p=%s,q=%s,e=%s"%(p1,q1,e1))
print("d is:\t%s"%d)
