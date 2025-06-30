#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    words = text.split()
    char_count = 0
    for word in words:
        for char in word:
            char_count += 1
    return char_count
