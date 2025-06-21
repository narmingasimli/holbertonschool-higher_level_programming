#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix and matrix != [[]]:
        print()
        return
    for row in matrix:
        if not row:
            print()
            continue
        formatted_elements = []
        for element in row:
            formatted_elements.append("{:d}".format(element))
        print(" ".join(formatted_elements))
