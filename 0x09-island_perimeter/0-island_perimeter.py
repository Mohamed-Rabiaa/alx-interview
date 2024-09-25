#!/usr/bin/python3
"""
This module contains the island_perimeter function
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    The grid is represented as a list of lists of integers:
    - 0 represents water.
    - 1 represents land.

    Each cell is a square with a side length of 1. Cells are connected
    horizontally or vertically (not diagonally). The grid is rectangular,
    with its width and height not exceeding 100. The grid is completely
    surrounded by water, and there is exactly one island or no island.
    The island has no lakes (water inside the island that is not connected
    to the surrounding water).

    Args:
        grid (List[List[int]]): A list of lists representing the grid,
        where 0 is water and 1 is land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2
    return perimeter
