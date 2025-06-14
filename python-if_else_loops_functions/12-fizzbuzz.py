#!/usr/bin/python3
def fizzbuzz():
    """
    Prints numbers from 1 to 100 according to the FizzBuzz rules.
    - Multiples of 3: Fizz
    - Multiples of 5: Buzz
    - Multiples of both 3 and 5: FizzBuzz
    Each element is followed by a space.
    """
    for i in range(1, 101):  # Loop from 1 to 100 (101 is exclusive)
        # Check for multiples of both 3 and 5 first
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:  # Check for multiples of 3
            print("Fizz", end=" ")
        elif i % 5 == 0:  # Check for multiples of 5
            print("Buzz", end=" ")
        else:  # If none of the above, print the number itself
            print(i, end=" ")
