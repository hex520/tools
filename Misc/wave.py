#! /usr/bin/env python3

import wave

import re

import numpy as np

# 打开WAV文档
path = "/home/hsm/Downloads/music.wav"
f = wave.open(path, "rb")

# 读取格式信息

# (nchannels, sampwidth, framerate, nframes, comptype, compname)

params = f.getparams()

nchannels, sampwidth, framerate, nframes = params[:4]

# 读取波形数据

str_data = f.readframes(nframes)
# print(str_data)

f.close()

#将波形数据转换为数组

wave_data = np.fromstring(str_data, dtype=np.short)
b = ''
# arr = [elem for elem in wave_data if elem >0]
# print("----")
max = 0
d = ''
for i in wave_data:
    if i <0:
        if max !=0:
            if max<25000:
                d +='0'
            else:
                d += '1'
                pass
        max = 0

    if max < i:
        max = i
# print(len(d))
print(d)
a = re.findall(r'.{8}',d)
for i in a:
    print(chr(int(i,2)),end='')

# print(b)

