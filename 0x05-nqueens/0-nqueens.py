#!/usr/bin/python3
"""
N Queens problem solved using backtracking.
This script places N queens on an N×N chessboard without them attacking each other.
"""

import sys


def print_board(board):
    """Print the board in the required output format."""
    print([[i, col] for i, col in enumerate(board)])


def is_safe(board, row, col):
    """
    Check if placing a queen at board[row] = col is safe.
    :param board: List of queen positions by row (index is row, value is column)
    :param row: Current row to place queen
    :param col: Column to place queen
    :return: True if safe, False otherwise
    """
    for i in range(row):
        # Check if there is a queen in the same column or diagonals
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_n_queens(board, row, n):
    """
    Recursively solve the N Queens problem.
    :param board: List of current queen positions
    :param row: Current row to place the queen
    :param n: Size of the board (N x N)
    """
    if row == n:
        print_board(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(board, row + 1, n)
            # No need to manually backtrack since the value is overwritten in the next iteration.


def main():
    """Main entry point of the program."""
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

    # Initialize the board with -1 (no queen placed)
    board = [-1] * n
    solve_n_queens(board, 0, n)


if __name__ == "__main__":
    main()
