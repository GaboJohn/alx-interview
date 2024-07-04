#!/usr/bin/env python3
"""
Solves the N-queens puzzle.
Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

Usage:
    $ ./0-nqueens.py N

N must be an integer greater than or equal to 4.
"""

import sys


def is_valid(board, row, col):
    """
    Check if a queen can be placed at board[row][col] without conflicts.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n, solutions):
    """
    Solve the N queens problem using backtracking.
    """
    if row == n:
        # If all queens are placed, add the solution
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)
            # Backtrack
            board[row] = -1


def main():
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

    # Initialize the board with -1 indicating no queens placed
    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
