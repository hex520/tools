def Exgcd(a, b):
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
        return x + n
    else:
        return x

p = 473398607161
q = 4511491
e = 17
N = p * q
phi_N = (p - 1) * (q - 1)
d = inv(e, phi_N)
print(e, N)#Private Key
print(d, N)#Public Key
