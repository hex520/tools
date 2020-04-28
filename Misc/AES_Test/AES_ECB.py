# -*- coding: utf-8 -*-
import hashlib
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

#MD5 加密
def md5Encode(key):
    Md5Cipher = hashlib.md5(key.encode(encoding="utf-8")).hexdigest()
    return Md5Cipher

#判断字符串长度是否等于16
def align(str, length = False):
    if len(str) > 16:
        return str[0:16]
    elif len(str) < 16:
        count = 16 - len(str.encode('utf-8')) % 16
        str = format(str) + format('\0'*count)
        return str
    else:
        return str

#ECB模式加密
def encrypt_ECB(str, key):
    str = align(str)
    key = align(key, True)
    #初始化AES
    EcbCipher =  AES.new(md5Encode(key).encode('utf-8'), AES.MODE_ECB)
    cipher = EcbCipher.encrypt(str)
    return b2a_hex(cipher)

# ECB模式解密
def decrypt_ECB(str, key):
    #补全字符串
    key = align(key, True)
    #初始化AES
    EcbCipher = AES.new(md5Encode(key).encode('utf-8'), AES.MODE_ECB)
    # 解密
    paint = EcbCipher.decrypt(a2b_hex(str)).decode('utf-8')
    return paint

if __name__=='__main__':
    key = input("请输入明文密钥: ")
    text = input("请输入需加密明文: ")
    # ECB模式加密
    ciphertext = encrypt_ECB(text, key)
    print("ECB模式密文：" + format(ciphertext))
    # ECB模式解密
    plaintext = decrypt_ECB(ciphertext, key)
    print("ECB模式明文：" + format(plaintext).replace('\0',''))