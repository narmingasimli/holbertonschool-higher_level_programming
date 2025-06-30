#!/usr/bin/python3
"""Function starting..."""


def read_file(filename=""):
    """FUnction begins from here."""
    with open(f"{filename}", encoding='UTF8') as f:
        print(f.read(), end="")
