#!/usr/bin/python3
def uppercase(str):
    """
    Prints a string in uppercase, followed by a new line.
    Args:
        str: The input string to be converted to uppercase.
    """
    print("{}".format("".join(
        chr(ord(char) - 32)
        if (ord('a') <= ord(char) <= ord('z'))
        else char
        for char in str
    )))
