# gmpy2是一个C编码的Python扩展模块，它支持多精度算术。gmpy2是原始gmpy模块的后继者。
import gmpy2
p = 473398607161
q = 4511491
e = 17

def rsaGmpy2(p,q,e):  #rsa加密,得到密钥d
    phi = (p-1)*(q-1)
    d = gmpy2.invert(e,phi)
    print(d)
rsaGmpy2(p,q,e)
# flag:cyberpeace{125631357777427553}

