#!/usr/bin/python3
"""
0-nqueens: A solution to the N-Queens problem using backtracking.
"""

import sys


def nqueens(n):
    """
    Solves the N-Queens problem for an n x n chessboard.

    The N-Queens problem is the challenge of placing N chess queens on an
    n x n chessboard so that no two queens threaten each other. This means
    that no two queens can share the same row, column, or diagonal.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        list of list: A list containing all possible solutions, where each
        solution is represented by a list of [row, column] positions of
        the queens.
    """
    col = set()
    posDiag = set()
    negDiag = set()
    solution = []
    solutions_list = []

    def backtrack(r):
        """
        Recursively attempts to place queens row by row.

        If a valid configuration is found (when all queens are placed),
        the solution is added to the solutions_list.

        Args:
            r (int): The current row to attempt placing a queen.
        """
        if r == n:
            solutions_list.append(solution.copy())  # Copy the current solution
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            solution.append([r, c])

            backtrack(r + 1)

            # Backtrack
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            solution.pop()

    backtrack(0)
    return solutions_list


if __name__ == '__main__':
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

    solutions = nqueens(n)
    for sol in solutions:
        print(sol)
