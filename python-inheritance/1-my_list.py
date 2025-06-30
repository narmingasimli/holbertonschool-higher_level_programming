#!/usr/bin/python3
"""
Module: 1-my_list
Description: Defines a class MyList that inherits from the built-in list class.
"""

class MyList(list):
    """
    MyList class inherits from 'list'.

    It provides a public instance method to print the list in sorted (ascending) order.
    The original list object remains unchanged after calling print_sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        This method creates a new sorted list from the current instance
        and prints its string representation to standard output.
        It does not modify the original list in place.
        """
        sorted_list = sorted(self)
        print(sorted_list)
