#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        division_result = 0
        try:
            val1 = my_list_1[i]
            val2 = my_list_2[i]
            division_result = float(val1) / float(val2)
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result.append(division_result)
    return result
