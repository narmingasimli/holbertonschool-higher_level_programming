#!/usr/bin/python3
def islower(c):
    """
    Checks for lowercase character.
    Args:
        c: The character to be checked.
    Returns:
        True if c is lowercase, False otherwise.
    """
    # Check if the ASCII value of the character 'c' falls within the
    # range of lowercase letters ('a' to 'z').
    # ord('a') gives the ASCII value of 'a' (97).
    # ord('z') gives the ASCII value of 'z' (122).
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False
