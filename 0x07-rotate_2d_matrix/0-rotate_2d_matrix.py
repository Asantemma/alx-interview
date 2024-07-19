#!/usr/bin/python
"""
ROtating a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a matrix 90 degrees clockwise in place.
    Args:
    matrix (list of list of int): The n x n 2D matrix to rotate
    """
    size = len(matrix)
    for layer in range(int(size / 2)):
        end = size - layer - 1
        for element in range(layer, end):
            offset = size - 1 - element
            # current number
            top = matrix[layer][element]
            # change top for left
            matrix[layer][element] = matrix[offset][layer]
            # change left for bottom
            matrix[offset][layer] = matrix[end][offset]
            # change bottom for right
            matrix[end][offset] = matrix[element][end]
            # change right for top
            matrix[element][end] = top
