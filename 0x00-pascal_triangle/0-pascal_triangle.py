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

        prow = row_index - 1
        for e_index in range(len(triangle[prow])):
            if e_index + 1 == len(triangle[prow]):
                # last element
                current_row.append(1)
                break
            # Add two previous values to get the current next value
            next_val = triangle[prow][e_index] + triangle[prow][e_index + 1]
            current_row.append(next_val)
        triangle.append(current_row)

    return triangle
