#!/usr/bin/python3
"""
Island perimeter computing module.
"""


def island_perimeter(grid):
    """
    Computes the perimeter of an island with no lakes.

    Args:
        grid (list of list of int): 2D grid where 1
        represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    if not isinstance(grid, list) or not all(isinstance(row, list) for row in grid):
        return 0

    perimeter = 0
    n = len(grid)

    for i in range(n):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Check top
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check right
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:
                    perimeter += 1
                # Check bottom
                if i == n - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1

    return perimeter
