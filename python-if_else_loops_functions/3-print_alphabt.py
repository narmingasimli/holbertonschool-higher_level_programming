#!/usr/bin/python3
print("{}".format("".join(chr(i) for i in range(97, 123)
                          if i not in [101, 113])), end="")
