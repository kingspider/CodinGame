import sys
import math

message = input()


def tobinary(strg):
    rtn = ""
    for char in strg:
        thisrtn = ""
        by = bin(ord(char))
        thisrtn += by[2:]
        print("Char: " + str(char) + " ASCII: " + str(ord(char)) +"  BIN :" + str(by) + " BIN-NP: "+ str(by[2:]), file=sys.stderr)
        if len(thisrtn) < 7:
            thisrtn = "0" + thisrtn
        rtn += thisrtn
    return rtn
      
    
def encode(strg):
    """Encode the binary string in blocks of 1(0 ) and 0(00 )"""
    
    current = 2
    rtn = ""
    if strg[0] == "0":
        current = 0
        rtn = rtn + "00 "
    elif strg[0] == "1":
        current = 1
        rtn = rtn + "0 "

    for bit in strg: 
        if current == 1:
            if bit == "1":
                rtn = rtn + "0"
            elif bit == "0":
                rtn = rtn + " 00 0"
                current = 0               
        elif current == 0:
            if bit == "1":
                rtn = rtn + " 0 0"
                current = 1
            elif bit == "0":
                rtn = rtn + "0"         
    return rtn


binarymessage = tobinary(message)
print(encode(binarymessage))