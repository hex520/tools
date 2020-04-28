# -*- coding: utf-8 -*-
import hashlib
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

#MD5 加密
def md5Encode(key):
    Md5Cipher = hashlib.md5(key.encode('utf-8')).hexdigest()
    return Md5Cipher

#判断字符串长度是否等于16
def align(str, length = False):
    if len(str) > 16:
        return str[0:16]
    elif len(str) < 16:
        count = 16 - len(str) % 16
        str = format(str) + format('\0'*count)
        return str
    else:
        return str

# ECB模式解密
def decrypt_ECB(str, key):
    # 补全字符串
    key = align(key, True)
    # 初始化AES
    EcbCipher = AES.new(md5Encode(key).encode('utf-8'), AES.MODE_ECB)
    # 解密
    paint = EcbCipher.decrypt(a2b_hex(str)).decode('utf-8')
    return paint

if __name__=='__main__':
    key = input(u"请输入明文密钥：")
    print(md5Encode(key))
    Text = input(u"\n请输入ECB密文：")
    # ECB模式解密
    try:
        plaintext = decrypt_ECB(Text, key)
        print(u"ECB模式明文：" + format(plaintext).replace('\0', ''))
    except UnicodeDecodeError as err:
        print(u"输入的密钥或密文有误!", )