#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary.values():
        new_dict[key] = value
    return new_dict
