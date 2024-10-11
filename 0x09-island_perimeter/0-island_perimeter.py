#!/usr/bin/python3
"""
Module that contains the function to calculate the perimeter of an island.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (List[List[int]]): A 2D list representing the island map.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Add 4 for the current land cell
                perimeter += 4

                # Check the cell above (row - 1, col)
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Shared edge with the top neighbor

                # Check the cell to the left (row, col - 1)
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Shared edge with the left neighbor

    return perimeter
