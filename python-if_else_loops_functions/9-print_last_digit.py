#!/usr/bin/python3
def print_last_digit(number):
    """
    Prints the last digit of a number and returns its value.
    Args:
        number: The integer whose last digit is to be printed and returned.
    Returns:
        The value of the last digit.
    """
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
