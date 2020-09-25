#!/bin/python3
import os
import sys

import binascii
from bitstring import BitArray
from arrays import obfuscation_array, InitialCode, XorMatrix, PadArray
from utils import findLSB, findMsb, log, create_password_verifier

password = "password123"

# FUNCTION CreateXorArray_Method1
# PARAMETERS Password
# RETURNS array of 8-bit unsigned integers
def create_xor_array_method1(password):
    # SET XorKey TO CreateXorKey_Method1(Password)
    xor_key = create_xor_key_method1(password)

    # SET Index TO Password.Length
    index = len(password)

    temp_obfuscation_array = list(obfuscation_array)

    # IF Index MODULO 2 IS 1
    if index % 2 == 1:
        # SET Temp TO most significant byte of XorKey
        temp = findMsb(xor_key)  # set temp to msb of xor_key

        # SET ObfuscationArray[Index] TO XorRor(PadArray[0], Temp)
        temp_obfuscation_array[index] = xor_ror(PadArray[0], temp)

        # DECREMENT Index
        index -= 1

        # SET Temp TO least significant byte of XorKey
        # temp = lsb of xor_key
        temp = findLSB(xor_key)

        # SET PasswordLastChar TO Password[Password.Length MINUS 1]
        password_last_char = password[len(password) - 1]

        # SET ObfuscationArray[Index] TO XorRor(PasswordLastChar, Temp)
        temp_obfuscation_array[index] = xor_ror(password_last_char, temp)

    # END IF
    # WHILE Index IS GREATER THAN to 0
    while index > 0:
        # DECREMENT Index
        index -= 1

        # SET Temp TO most significant byte of XorKey
        temp = findMsb(xor_key)

        byte_password_at_index = ord(password[index])

        # SET ObfuscationArray[Index] TO XorRor(Password[Index], Temp)
        temp_obfuscation_array[index] = xor_ror(byte_password_at_index, temp)

        # DECREMENT Index
        index -= 1

        # SET Temp TO least significant byte of XorKey
        temp = findLSB(xor_key)

        # SET ObfuscationArray[Index] TO XorRor(Password[Index], Temp)
        temp_obfuscation_array[index] = xor_ror(password[index], temp)

        # END WHILE

    # SET Index TO 15
    index = 15

    # SET PadIndex TO 15 MINUS Password.Length
    pad_index = 15 - len(password)

    # WHILE PadIndex IS greater than 0
    while pad_index > 0:
        # SET Temp TO most significant byte of XorKey
        temp = findMsb(xor_key)

        # SET ObfuscationArray[Index] TO XorRor(PadArray[PadIndex], Temp
        obfuscation_array[index] = xor_ror(PadArray[pad_index], temp)

        # DECREMENT Index
        index -= 1

        # DECREMENT PadIndex
        pad_index -= 1

        # SET Temp TO least significant byte of XorKey
        temp = findLSB(xor_key)

        # SET ObfuscationArray[Index] TO XorRor(PadArray[PadIndex], Temp)
        obfuscation_array[index] = xor_ror(PadArray[pad_index], temp)

        # DECREMENT Index
        index -= 1

        # DECREMENT PadIndex
        pad_index -= 1

    # END WHILE
    # RETURN ObfuscationArray
    return obfuscation_array


# FUNCTION CreateXorKey_Method1
# PARAMETERS Password
# RETURNS 16-bit unsigned integer
# DECLARE XorKey AS 16-bit unsigned integer
def create_xor_key_method1(password):
    # SET XorKey TO InitialCode[Password.Length MINUS 1]
    xor_key = list(InitialCode)[len(password) - 1]
    # log(xor_key)

    # SET CurrentElement TO 0x00000068
    current_element = 0x00000068

    # FOR EACH Char IN Password IN REVERSE ORDER
    for char in password[::-1]:
        # FOR 7 iterations
        # IF (Char BITWISE AND 0x40) IS NOT 0
        if char and 0x40 != 0:
            # SET XorKey TO XorKey BITWISE XOR XorMatrix[CurrentElement]
            xor_key = int(xor_key) ^ XorMatrix[current_element]
        # END IF
        else:
            # SET Char TO Char MULTIPLIED BY 2
            char = char * 2
            # DECREMENT CurrentElement
            current_element - 1
        return xor_key
    # END FOR

    # RETURN XorKey


# END FUNCTION

# FUNCTION XorRor
# PARAMETERS byte1, byte2
# RETURNS 8-bit unsigned integer
def xor_ror(byte1, byte2):
    # RETURN Ror(byte1 XOR byte2)
    if type(byte1) == int:
        pass
    else:
        byte1 = int(ord(byte1))

    if type(byte2) == int:
        pass
    else:
        byte2 = int(ord(byte2))

    byte3 = byte1 ^ byte2
    return byte3


# END FUNCTION

# FUNCTION Ror
# PARAMETERS byte
# RETURNS 8-bit unsigned integer


def ror(byte):  # byte is not being manipulated

    # SET temp1 TO byte DIVIDED BY 2
    temp1 = int(byte) / 2
    # SET temp2 TO byte MULTIPLIED BY 128
    temp2 = byte * 128
    # SET temp3 TO temp1 BITWISE OR temp2
    temp3 = int(temp1) | int(temp2)

    # RETURN temp3 MODULO 0x100
    return temp3 % 0x100


# END FUNCTION

# def encrypt_data(password, data, XorArrayIndex):
data = bytearray(8)


def encrypt_data(password, data, XorArrayIndex):
    # SET XorArray TO CreateXorArray_Method1(Password)
    xor_array = create_xor_array_method1(password)

    # FOR Index FROM 0 TO Data.Length
    for index in range(len(data)):
        # SET Value TO Data[Index]
        value = data[index]
        # SET Value TO (Value rotate left 5 bits)
        value = value << 5
        # SET Value TO Value BITWISE XOR XorArray[XorArrayIndex]
        value = value ^ xor_array[XorArrayIndex]
        # SET DATA[Index] TO Value
        data[index] = value

        # INCREMENT XorArrayIndex
        XorArrayIndex += 1
        # SET XorArrayIndex TO XorArrayIndex MODULO 16
        XorArrayIndex = XorArrayIndex % 16
    # END FOR


# END FUNCTION

# FUNCTION DecryptData_Method1
# RPARAMETERS Password, Data, XorArrayIndex
def decrypt_data_method1(password, data, XorArrayIndex):
    # SET XorArray TO CreateXorArray_Method1(Password)
    xor_array = create_xor_array_method1(password)
    # FOR Index FROM 0 to Data.Length
    for index in range(len(data)):
        # SET Value TO Data[Index]
        value = data[index]
        # SET Value TO Value BITWISE XOR XorArray[XorArrayIndex]

        value = value ^ xor_array[XorArrayIndex]
        # SET Value TO (Value rotate right 5 bits)
        value = value >> 5

        # SET Data[Index] TO Value
        data[index] = int(value)

        # INCREMENT XorArrayIndex
        XorArrayIndex += 1
        # SET XorArrayIndex TO XorArrayIndex MODULO 16
        XorArrayIndex = XorArrayIndex % 16
    # END FOR
    return data


# END FUNCTION


if __name__ == "__main__":
    excel_filename = sys.argv[1]
    data = []
    with open(excel_filename, "rb") as f:
        while (byte := f.read(1)) :
            data.append(int.from_bytes(byte, byteorder="big"))

    decrypted_data = decrypt_data_method1("password123", data, 0)
    # log(decrypted_data)
    # log(bytearray(decrypted_data))
    #     # make file
    # newFile = open("filename.txt", "wb")
    # # write to file
    # newFile.write(newFileBytes)
    log(create_password_verifier(password))
    # log(create_xor_array_method1(password))
    # log(create_xor_key_method1(password))