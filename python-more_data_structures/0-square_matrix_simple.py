#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for line in matrix:
        new_line = [x ** 2 for x in line]
        new_matrix.append(new_line)
        
    return new_matrix