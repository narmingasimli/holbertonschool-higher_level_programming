#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Ədədin son rəqəmini hesabla.
# Müsbət ədədlər üçün number % 10, mənfi ədədlər üçün number % -10 istifadə edirik
# ki, son rəqəmin işarəsi də ədədin işarəsi ilə eyni olsun.
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

# Şərtləri yoxla və çıxışı çap et.
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:  # last_digit < 6 and not 0
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
