

import re
str = "0F0004432C8106"
str = "6520666C61672069733A0D0A0000704700BFFEE700BFFEE700BFFEE7"
str = "22405468"
str2 = "6520666C616720"
str3 = "69733A0D0A0000"
str4 = "704700BFFEE700BFFEE700BFFEE700BFFEE77047704770477047"
#
# 25
# 26
# 2700BFFEE7704770
# 2847704770470000
# 3008000000000000
def hexToString(string):
    arr = re.findall(r'.{2}',string)
    for i in arr:
        result = int(i,16)
        print(chr(result),end='')
hexToString(str)
hexToString(str2)
hexToString(str3)
hexToString(str4)
print(int('1e',16))
# 236520666C616720
# 2469733A0D0A0000
# 25704700BFFEE700
# 26BFFEE700BFFEE7
# 2700BFFEE7704770
# 2847704770470000
# 3008000000000000