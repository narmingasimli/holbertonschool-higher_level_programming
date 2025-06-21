#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_new_list = set(my_list)
    sum = 0
    for number in my_new_list:
        sum += number
    return sum
