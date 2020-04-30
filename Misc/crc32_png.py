import os
import binascii
import struct
import json
filename = "flag.png"
crc = 0x7bc0ae5a
download = "/home/hsm/Downloads/"
filename = download+filename

def width(filename,crc):
    file = open(filename, "rb").read()
    for i in range(5120):
        data = file[12:16] + struct.pack('>i', i) + file[20:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        if crc32 == crc:
            print("width:" + hex(i))



def heigh(filename,crc):
    file = open(filename, "rb").read()
    for i in range(5120):
        data = file[12:20] + struct.pack('>i', i) + file[24:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        if crc32 == crc:
            print("heigh:" + hex(i))
width(filename,crc)
heigh(filename,crc)
