#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        division_result = 0.0
        try:
            val1 = my_list_1[i]
            val2 = my_list_2[i]
            val1 + 0
            val2 + 0
            division_result = float(val1) / float(val2)
        except TypeError:
            print("wrong type")
            division_result = 0.0
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0.0
        except IndexError:
            print("out of range")
            division_result = 0.0
        finally:
            result.append(division_result)
    return result
