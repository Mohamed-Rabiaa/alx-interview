#!/usr/bin/python3
"""
This module contains the pascal_triangle function
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the n-th row.

    Pascal's Triangle is a triangular array of the binomial coefficients.
    The rows of Pascal's Triangle are conventionally enumerated starting
    with row 0 at the top (the 0th row).

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list of list of int: A list of lists representing Pascal's Triangle
                             up to the n-th row. Each inner list represents
                             a row in the triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        current_row = [1]
        if triangle:
            last_row = triangle[-1]
            current_row.extend([last_row[j] + last_row[j + 1]
                                for j in range(len(last_row) - 1)])
            current_row.append(1)
        triangle.append(current_row)

    return triangle
