import re
str = "ababaa"
def hexToString(string):
    arr = re.findall(r'.{2}',str)
    for i in arr:
        result = int(i,16)
        print(chr(result))
hexToString(str)