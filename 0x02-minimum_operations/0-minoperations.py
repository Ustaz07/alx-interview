#!/usr/bin/python3
"""
Module 0-minoperations
Contains a method that cal the few no of oper need to result in n H char.
"""


def minOperations(n):
    """Calculate the min no of oper. to get exactly n 'H' characters."""
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
