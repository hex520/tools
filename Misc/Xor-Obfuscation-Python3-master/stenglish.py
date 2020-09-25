FUNCTION CreatePasswordVerifier_Method1 PARAMETERS Password
    SET Verifier TO 0x0000
    SET PasswordArray TO (empty array of bytes) 
    SET PasswordArray[0] TO Password.Length 
    APPEND Password TO PasswordArray
    
    FOR EACH PasswordByte IN PasswordArray IN REVERSE ORDER 
        IF (Verifier BITWISE AND 0x4000) is 0x0000
            SET Intermediate1 TO 0
        ELSE
            SET Intermediate1 TO 1
        ENDIF
        
        SET Intermediate2 TO Verifier MULTIPLED BY 2 
        SET most significant bit of Intermediate2 TO 0
        
        SET Intermediate3 TO Intermediate1 BITWISE OR Intermediate2
        SET Verifier TO Intermediate3 BITWISE XOR PasswordByte 
    ENDFOR
    
    RETURN Verifier BITWISE XOR 0xCE4B
END FUNCTION


FUNCTION CreateXorArray_Method1
    PARAMETERS Password
    RETURNS array of 8-bit unsigned integers

    DECLARE XorKey AS 16-bit unsigned integer
    DECLARE ObfuscationArray AS array of 8-bit unsigned integers

    SET XorKey TO CreateXorKey_Method1(Password)

    SET Index TO Password.Length
    SET ObfuscationArray TO (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)

    IF Index MODULO 2 IS 1
        SET Temp TO most significant byte of XorKey
        SET ObfuscationArray[Index] TO XorRor(PadArray[0], Temp)

                DECREMENT Index
                
        SET Temp TO least significant byte of XorKey
        SET PasswordLastChar TO Password[Password.Length MINUS 1] 
        SET ObfuscationArray[Index] TO XorRor(PasswordLastChar, Temp)
    END IF

    WHILE Index IS GREATER THAN to 0
        DECREMENT Index
        SET Temp TO most significant byte of XorKey
        SET ObfuscationArray[Index] TO XorRor(Password[Index], Temp)

        DECREMENT Index
        SET Temp TO least significant byte of XorKey
        SET ObfuscationArray[Index] TO XorRor(Password[Index], Temp) 
    END WHILE

    SET Index TO 15
    SET PadIndex TO 15 MINUS Password.Length 
    WHILE PadIndex IS greater than 0

        SET Temp TO most significant byte of XorKey
        SET ObfuscationArray[Index] TO XorRor(PadArray[PadIndex], Temp) 
        DECREMENT Index
        DECREMENT PadIndex

        SET Temp TO least significant byte of XorKey
        SET ObfuscationArray[Index] TO XorRor(PadArray[PadIndex], Temp) 
        DECREMENT Index
        DECREMENT PadIndex
    END WHILE

    RETURN ObfuscationArray
END FUNCTION

FUNCTION CreateXorKey_Method1 
    PARAMETERS Password
    RETURNS 16-bit unsigned integer

    DECLARE XorKey AS 16-bit unsigned integer

    SET XorKey TO InitialCode[Password.Length MINUS 1] 

    SET CurrentElement TO 0x00000068

    FOR EACH Char IN Password IN REVERSE ORDER 
        FOR 7 iterations
            IF (Char BITWISE AND 0x40) IS NOT 0
                SET XorKey TO XorKey BITWISE XOR XorMatrix[CurrentElement]
            END IF
            SET Char TO Char MULTIPLIED BY 2
            DECREMENT CurrentElement
        END FOR
    END FOR

    RETURN XorKey
END FUNCTION

FUNCTION XorRor
    PARAMETERS byte1, byte2 
    RETURNS 8-bit unsigned integer

    RETURN Ror(byte1 XOR byte2)
END FUNCTION

FUNCTION Ror
    PARAMETERS byte
    RETURNS 8-bit unsigned integer
    
    SET temp1 TO byte DIVIDED BY 2
    SET temp2 TO byte MULTIPLIED BY 128
    SET temp3 TO temp1 BITWISE OR temp2
    RETURN temp3 MODULO 0x100
END FUNCTION


FUNCTION EncryptData_Method1
    PARAMETERS Password, Data, XorArrayIndex
    DECLARE XorArray as array of 8-bit unsigned integers

    SET XorArray TO CreateXorArray_Method1(Password)

    FOR Index FROM 0 TO Data.Length
        SET Value TO Data[Index]
        SET Value TO (Value rotate left 5 bits)
        SET Value TO Value BITWISE XOR XorArray[XorArrayIndex] SET DATA[Index] TO Value
                INCREMENT XorArrayIndex
        SET XorArrayIndex TO XorArrayIndex MODULO 16 
    END FOR
END FUNCTION


FUNCTION DecryptData_Method1
    RPARAMETERS Password, Data, XorArrayIndex
    DECLARE XorArray as array of 8-bit unsigned integers

    SET XorArray TO CreateXorArray_Method1(Password)

    FOR Index FROM 0 to Data.Length
        SET Value TO Data[Index]
        SET Value TO Value BITWISE XOR XorArray[XorArrayIndex] SET Value TO (Value rotate right 5 bits)
        SET Data[Index] TO Value
            
        INCREMENT XorArrayIndex
        SET XorArrayIndex TO XorArrayIndex MODULO 16 
    END FOR
END FUNCTION