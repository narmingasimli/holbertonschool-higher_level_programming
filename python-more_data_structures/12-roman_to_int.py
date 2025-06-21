#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_values = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500,
        'M': 1000
    }
    result = 0
    length = len(roman_string)
    for i in range(length - 1):
        current = roman_values.get(roman_string[i], 0)
        next_ = roman_values.get(roman_string[i + 1], 0)

        if current >= next_:
            result += current
        else:
            result -= current
    result += roman_values.get(roman_string[-1], 0)
    return result
