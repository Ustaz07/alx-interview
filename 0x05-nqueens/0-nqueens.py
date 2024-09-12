#!/usr/bin/python3
""" N queens """
import sys

# Check the number of command-line arguments
if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

# Check if the argument is a digit
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

# Check if the number is at least 4
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

# Convert the input to an integer
n = int(sys.argv[1])

def queens(n, i=0, a=[], b=[], c=[]):
    """ Find all possible positions of queens on the board """
    if i < n:
        for j in range(n):
            # Check if the position is safe: not in the same column, major, or minor diagonal
            if j not in a and i + j not in b and i - j not in c:
                # Recursively place the next queen
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        # Yield the current valid solution
        yield a

def solve(n):
    """ Solve the N queens problem and print each solution """
    # Initialize variables to store each solution
    k = []
    i = 0
    # Generate and print each solution
    for solution in queens(n, 0):
        for s in solution:
            # Collect the positions of the queens
            k.append([i, s])
            i += 1
        print(k)
        # Reset the position list and index for the next solution
        k = []
        i = 0

# Start solving
solve(n)
