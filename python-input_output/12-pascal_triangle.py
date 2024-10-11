#!/usr/bin/python3
"""Module 12-pascal_triangle: Define pascal triangle"""


def pascal_triangle(n):
    """generate pascal tringle of size n"""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        """create a new row in the triangle for row number"""
        row = [1]
        for j in range(1, i):
            """Determine the value for the current position in the row"""
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
