#!/usr/bin/python3
"""
0x1C. Island Perimeter, task 0. Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (list of lists of ints): 2D list representation of the island map.
            - 0 represents water.
            - 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                # Check for water or edges in all four directions.
                if x == 0 or grid[y][x - 1] == 0:  # Left
                    perimeter += 1
                if x == len(grid[0]) - 1 or grid[y][x + 1] == 0:  # Right
                    perimeter += 1
                if y == 0 or grid[y - 1][x] == 0:  # Top
                    perimeter += 1
                if y == len(grid) - 1 or grid[y + 1][x] == 0:  # Bottom
                    perimeter += 1
    return perimeter
