

import re
str1 = "64010602010000000014"


def hexToString(string):
    arr = re.findall(r'.{2}',string)
    for i in arr:
        result = int(i,16)
        print(chr(result),end='')
hexToString(str1)

