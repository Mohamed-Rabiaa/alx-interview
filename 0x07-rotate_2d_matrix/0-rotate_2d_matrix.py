#!/usr/bin/python3
"""
This module contains the rotate_2d_matrix function
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degress clockwise

    Args:
        matrix: the 2D matrix to rotate
    """
    # Transposing the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reversing the rows in the matrix
    for row in matrix:
        row.reverse()
