import os
import binascii
import struct
import json

# 所以无奈决定，直接通过读取png文件头来获取文件大小
#
# 00000000h: 89 50 4E 47 0D 0A 1A 0A00 00 00 0D49 48 44 52 ; 塒NG........IHDR
# 00000010h: 00 00 00 CE 00 00 00 CE 08 02 00 00 00 F9 7D AA ; ...?..?....鶀?
# 00000020h: 93 00 00 00 09 70 48 59 73 00 00 0A 75 00 00 0A ; ?...pHYs...u...
# 00000030h: 75 01 4A 25 DD FD 00 00 0C 91 49 44 41 54 78 9C ; u.J%蔟...慖DATx?
# 00000040h: ED 9D D9 96 DC 2A 0C 45 A9 AC FC FF 2F D7 7D 70 ; 頋贃?.E┈?/讅p
# 00000050h: C7 97 66 10 9A 98 CF 7E C8 EA 54 95 6D 86 83 24 ; 菞f.殬蟸汝T昺唭$
# 00000060h: 04 B6 3F DF EF 37 00 D0 9F 3F B3 0B 00 6E 01 52 ; .?唢7.袩??.n.R
# 00000070h: 03 83 F8 3B BB 00 AB F2 F9 98 0E 47 58 92 01 A9 ; .凐;?鶚.GX?? 
#
# 89 50 4E 47 0D 0A 1A 0A 是PNG头部署名域，表示这是一个PNG图片
# 00 00 00 0D 描述IHDR头部的大小
# 49 48 44 52 是Chunk Type Code, 这里Chunk Type Code=IHDR
# 00 00 00 CE 00 00 00 CE 08 02 00 00 00 描述了Chunk Data，它是可变长度数据，00 00 00 0D 定义了长度为13个Bytes，所以,这里，你看到是13个字节)
# F9 7D AA 93 是对IHDR的CRC校验


filename = "dabai.png"
crc = 0x6d7c7135
download = "/home/hsm/Downloads/"
filename = download+filename

def width(filename,crc):
    file = open(filename, "rb").read()
    for i in range(10240):
        data = file[12:16] + struct.pack('>i', i) + file[20:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        if crc32 == crc:
            print("width:" + hex(i))

def heigh(filename,crc):
    file = open(filename, "rb").read()
    for i in range(10240):
        data = file[12:20] + struct.pack('>i', i) + file[24:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        if crc32 == crc:
            print("heigh:" + hex(i))
width(filename,crc)
heigh(filename,crc)
