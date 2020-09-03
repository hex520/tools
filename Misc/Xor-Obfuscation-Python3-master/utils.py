from termcolor import colored
from inspect import currentframe


def log(value):
    frameinfo = currentframe()
    line_formatted = "line:{}".format(frameinfo.f_back.f_lineno)
    print(colored(value, "yellow"), colored(line_formatted, "blue"))


# FUNCTION CreatePasswordVerifier_Method1 PARAMETERS Password
def create_password_verifier(password):
    # SET Verifier TO 0x0000
    verifier = 0x0000
    # log(verifier)
    # SET PasswordArray TO (empty array of bytes)
    password_array = bytearray()
    # log(password_array)
    password_array.append(len(password))
    # log(password_array)
    password = binascii.unhexlify(password)
    password_array.extend(password)
    # log(type(password_array))
    password_array.reverse()
    # log(password_array)

    # FOR EACH PasswordByte IN PasswordArray IN REVERSE ORDER
    for password_byte in password_array:
        intermediate1 = 0
        # log(password_byte)
        # IF (Verifier BITWISE AND 0x4000) is 0x0000
        if verifier & 0x4000 == 0x0000:
            intermediate1 = 0
            # SET Intermediate1 TO 0
        # ELSE
        else:
            # SET Intermediate1 TO 1
            intermediate1 = 1
        # ENDIF

        # SET Intermediate2 TO Verifier MULTIPLED BY 2
        intermediate2 = verifier * 2
        # SET most significant bit of Intermediate2 TO 0 #will come back to
        intermediate2 = setMSBto0(0)
        # SET Intermediate3 TO Intermediate1 BITWISE OR Intermediate2
        intermediate3 = intermediate1 ^ intermediate2
        # SET Verifier TO Intermediate3 BITWISE XOR PasswordByte
        verifier = intermediate3 ^ password_byte

        # ENDFOR

    # RETURN Verifier BITWISE XOR 0xCE4B
    return verifier ^ 0xCE4B


# END FUNCTION


def findMsb(n):
    if n == 0:
        return 0

    msb = 0
    while n > 0:
        n = int(n / 2)
        msb += 1

    return 1 << msb


def findLSB(n):
    return n & -n


def setMSBto0(n):
    if n == 1:
        return 0
    result = lambda n: int("0" + bin(n)[3:], 2)
    return result(n)
