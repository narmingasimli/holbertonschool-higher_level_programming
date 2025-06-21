#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        division_result = 0  # Initialize as an integer 0
        try:
            val1 = my_list_1[i]
            val2 = my_list_2[i]
            division_result = float(val1) / float(val2)
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0  # Set to integer 0 for division by zero error
        except (TypeError, ValueError):
            print("wrong type")
            division_result = 0  # Set to integer 0 for type/value errors
        except IndexError:
            print("out of range")
            division_result = 0  # Set to integer 0 for out of range errors
        finally:
            result.append(division_result)
    return result
