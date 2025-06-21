#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value == int:
            return value
    except TypeError:
        pass
    print()
