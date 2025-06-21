#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]  # skip the script name
    count = len(argv)
    if count == 0:
        print("0 arguments.")
    else:
        word = "argument" if count == 1 else "arguments"
        print(f"{count} {word}:")

        for i in range(count):
            print(f"{i + 1}: {argv[i]}")
