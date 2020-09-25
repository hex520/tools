# -*- coding: utf-8 -*-
import hashlib
import sys

#MD5 加密,明文key需要先编码为utf-8
def md5Encode(key):
    Md5Cipher = hashlib.md5(key.encode('utf-8')).hexdigest()
    return Md5Cipher

#key = input(u"请输入明文密钥：")
#print(md5Encode(key).upper())
key = md5Encode(sys.argv[1])
print(key.upper())
