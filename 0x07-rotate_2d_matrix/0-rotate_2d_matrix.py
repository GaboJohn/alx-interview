#!/usr/bin/python3
"""Module to rotate a 2D matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise.
    The matrix is edited in-place.
    Args:
        matrix (list of list of int): The 2D matrix to rotate.
    """
    n = len(matrix)
    left, right = 0, n - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            # Save the top-left value
            top_left = matrix[top][left + i]

            # Move bottom-left to top-left
            matrix[top][left + i] = matrix[bottom - i][left]

            # Move bottom-right to bottom-left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # Move top-right to bottom-right
            matrix[bottom][right - i] = matrix[top + i][right]

            # Move top-left to top-right
            matrix[top + i][right] = top_left

        left += 1
        right -= 1
