binStr = b'0110011001101100011000010110011101111011001101000100010001010011010111110011000101101110010111110100010000110001011100110110101101111101'
binStr = b"10101010101010101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101111111101111111101100101001000"
binStr = b"000000000000000000000001000001000100000011100000010001010000000001111000000000001110000010000010001010000000001100000001000101000000000110000000100010000010000000000100000110000010000001110000100111000001000001000101000000000111000000001100000010000000000100000000000010000010010000010100100000011100000000110000001000000001011000000"

binStr = b'01101011011011110110010101101011011010100011001101110011'
binStr = b'01000010010010100100010001111011010011010010000101100001001100000111111001111101'
def ToStr(binStr):
    i=0
    while i<len(binStr):
        b = chr(int(binStr[i:i+8],2))
        print(b,end='')
        i+=8


        
ToStr(binStr)
# str  "UUMM M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M M7"
# str = str.replace(' ','')
# print()
# print(str)


#string = "asfd"

