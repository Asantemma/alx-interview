#!/usr/bin/python3

"""This script solves the N queens problem using a backtracking algorithm."""

import sys


def solve_nqueens(n):
    """Solves the N queens puzzle using backtracking.

    Args:
        n (int): Number of queens and the size of the board (n x n).

    Returns:
        List[List[int]]: A list of solutions, where each solution is a list
        of [row, column] positions for the queens.
    """
    results = []

    def is_safe(row, col, queens_positions):
        """Checks if a queen can be placed at
        (row, col) without being attacked.
        """
        for r in range(row):
            if abs(col - queens_positions[r]) == row - r:
                return False
        return True

    def save_solution(queens_positions):
        """Saves the current valid positions of queens."""
        solution = []
        for r in range(n):
            solution.append([r, queens_positions[r]])
        results.append(solution)

    def place_queens(row, columns, queens_positions):
        """Places queens on the board recursively."""
        if row == n:
            save_solution(queens_positions)
            return

        for col in range(n):
            if columns[col] == 0 and is_safe(row, col, queens_positions):
                columns[col] = 1
                queens_positions[row] = col
                place_queens(row + 1, columns, queens_positions)
                columns[col] = 0

    place_queens(0, [0] * n, [0] * n)
    return results


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
