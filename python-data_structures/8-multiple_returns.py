#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = None  # Default to None for empty string
    if length > 0:
        first_char = sentence[0]
    return (length, first_char)
