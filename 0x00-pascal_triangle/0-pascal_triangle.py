#!/usr/bin/python3
"""A function that generates the pascal triangle
"""


def pascal_triangle(n):
    """Returns Pascal's triangle up to the nth row."""
    if n <= 0:
        return []

    triangle = []

    for row_index in range(n):
        current_row = [1]
        if row_index == 0:
            triangle.append(current_row)
            continue

        previous_row_index = row_index - 1
        for element_index in range(len(triangle[previous_row_index])):
            if element_index + 1 == len(triangle[previous_row_index]):
                # last element
                current_row.append(1)
                break
            # Add two previous values to get the current next value
            next_value = triangle[previous_row_index][element_index] + triangle[previous_row_index][element_index + 1]
            current_row.append(next_value)
        triangle.append(current_row)

    return triangle
