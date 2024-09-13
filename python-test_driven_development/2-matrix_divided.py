#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: List of lists of integers or floats.
        div: The divisor, must be a number (integer or float).

    Returns:
        A new matrix with all elements divided by the divisor and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if the rows of the matrix do not have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    
    if (not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(elem, (int, float)) for row in matrix for elem in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
