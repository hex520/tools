#! /usr/bin/env python3

import re
str1 = "64010602010000000014"
str1 = "79616E7A69205A4A517B78696C7A765F6971737375686F635F73757A6A677D20"

def hexToString(string):
    arr = re.findall(r'.{2}',string)
    for i in arr:
        result = int(i,16)
        print(chr(result),end='')
hexToString(str1)

