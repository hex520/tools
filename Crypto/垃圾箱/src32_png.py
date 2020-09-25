import os
import binascii
import struct
fileBath = ""
misc = open(fileBath,"rb").read()
for i in range(1024):
    data = misc[12:16] + struct.pack('>i',i)+ misc[20:29]
    crc32 = binascii.crc32(data) & 0xffffffff
    if crc32 == 0x932f8a6b:
        print(i)
        print("hex:"+hex(i))
