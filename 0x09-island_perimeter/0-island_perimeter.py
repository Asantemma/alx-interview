#!/usr/bin/python3
"""
Island perimeter function module
"""


def island_perimeter(grid):
    """Calculate the perimeter of the island in the grid.

    Args:
        grid (list[list[int]]): A 2D grid representing the map

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check all four directions
                if row == 0 or grid[row - 1][col] == 0:  # Check above
                    perimeter += 1
                if row == rows - 1 or grid[row + 1][col] == 0:  # Check below
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:  # Check left
                    perimeter += 1
                if col == cols - 1 or grid[row][col + 1] == 0:  # Check right
                    perimeter += 1

    return perimeter
