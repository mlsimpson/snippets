#!/usr/bin/env python

def encode_rle(inputString):
    # TODO: check if invalid input

    counter = 0
    prevChar = 0
    encodedString = ""

    for currChar in inputString:
        # string run is going
        if currChar == prevChar:
            counter += 1
        # we hit a break, currChar is no longer prevChar
        else:
            if prevChar != 0:
                encodedString = encodedString + str(counter) + prevChar
            # encode the string
            # set prevChar to currChar and increment counter
            prevChar = currChar
            counter = 1

    # finalize encoded string with "prevChar", the last char found
    encodedString = encodedString + str(counter) + prevChar
    print(encodedString)
    return encodedString


def decode_rle(inputString):
    # TODO: check if invalid input
    decodedString = ""
    rle_digit = ""

    for c in inputString:
        if c.isdigit():
            rle_digit = rle_digit + c
        else:
            rle_digit = int(rle_digit)
            decodedString = decodedString + (c * rle_digit)
            rle_digit = ""

    print(decodedString)
    return decodedString


encode_rle("abbccdd")

decode_rle("10a2b2c2d")

