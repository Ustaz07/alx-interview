#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n.
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            c = 1  # Changed variable name to lowercase to follow PEP 8
            for j in range(1, i + 1):
                level.append(c)
                c = c * (i - j) // j
            res.append(level)
    return res
