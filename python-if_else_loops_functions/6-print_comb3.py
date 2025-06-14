#!/usr/bin/python3
for i in range(10):  # First digit from 0 to 9
    for j in range(i + 1, 10):  # Second digit from i+1 to 9 (must be larger)
        num_combination = i * 10 + j  # Combine digits into a two-digit number
        if i == 8 and j == 9:
            print("{:02d}".format(num_combination), end="")
        else:
            print("{:02d}".format(num_combination), end=", ") # No trailing whitespace here
print("")
