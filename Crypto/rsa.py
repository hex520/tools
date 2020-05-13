import math
# 在一次RSA密钥对生成中，假设p=473398607161，q=4511491，e=17
# 求解出d
# 第一步，随机选择两个不相等的质数p和q。
# 选择473398607161和4511491。（实际应用中，这两个质数越大，就越难破解。）
p = 473398607161
q = 4511491
# 第二步，计算p和q的乘积n。
n = p*q
# n的长度就是密钥长度。n写成二进制是111011...1011010101011，一共有63位，
# 所以这个密钥就是63位。实际应用中，RSA密钥一般是1024位，重要场合则为2048位。

# 第三步，计算n的欧拉函数[N]φ(n)。
phi_N = (p-1)*(q-1)
# 第四步，随机选择一个整数e，条件是1< e < [N]φ(n)，且e与φ(n) 互质。
# 这里选择e=17,可以在1<e<N里面选择
e=17

# 第五步，求d，就是计算e对于[N]φ(n)的模反元素d。
# 所谓"模反元素"就是指有一个整数d，可以使得ed被[N]φ(n)除的余数为1
# 　e*d ≡ 1 (mod N) 等价
# 这个式子等价于
# 　ed - 1 = k*N,k是一个正整数
def Exgcd(a, b):# e , N
# ax+by=1,gcd(a,b)
    if b == 0:
        return (1, 0, a)
    (x, y, r) = Exgcd(b, a % b)
    temp = x
    x = y
    y = temp - a / b * y
    return (x, y, r)


def inv(a, n):
    # ax = 1 mod n
    (x, y, r) = Exgcd(a, n)
    if x < 0:
        return (x + n)
    else:
        return x
p = 473398607161
q = 4511491
e = 17
N = p * q
phi_N = (p - 1) * (q - 1)
d = inv(e,phi_N)
print(d)
print(e,phi_N)
print(d,phi_N)
# 针对随机取得p，q两个数的素性检测

# key = 125631357777427553

def a_b_mod(a,b):
    if a>b:
        max = a
        min = b
    else:
        max = b
        min = a
    while max%min!=0:
        tmp = max%min
        if tmp>min:
            max = tmp
        else :
            max = min
            min = tmp
    return min
result = a_b_mod(10,120)
print(result)
def ext_euclid(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = ext_euclid(b, a % b)
        # q = gcd(a, b) = gcd(b, a%b)
        x, y = y, (x - (a // b) * y)
        return x, y, q

print(ext_euclid(e,phi_N))