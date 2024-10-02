#!/usr/bin/python3
"""Module 12-pascal_triangle: Define pascal triangle"""


def pascal_triangle(n):
    """generate pascal tringle of size n"""
    if n <= 0:
        return []

    triangle = []
    for num_row in range(n):
        """create a new row in the triangle for row number"""
        row = []

        for col_num in range(num_row + 1):
            """Determine the value for the current position in the row"""
            if col_num == 0 or col_num == num_row:
                row.append(1)
            else:
                row.append(triangle[num_row - 1][col_num -
                           1] + triangle[num_row - 1][col_num])

        triangle.append(row)

    return triangle
