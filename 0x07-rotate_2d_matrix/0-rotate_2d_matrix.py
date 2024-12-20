#!/usr/bin/python3
"""
Rotate 2D Matrix module
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The 2D matrix to rotate.

    Returns:
        None. The matrix is modified in place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):  # Only traverse the upper triangle
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row to achieve the 90-degree rotation
    for row in matrix:
        row.reverse()
