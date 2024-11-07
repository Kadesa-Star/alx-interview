#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at board[row][col]."""
    for i in range(row):
        # Check column and both diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row=0, board=[]):
    """Solve the N Queens problem using backtracking."""
    if row == N:
        # Print solution as list of positions [[row, col], ...]
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board.append(col)
            solve_nqueens(N, row + 1, board)
            board.pop()  # Backtrack


def main():
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solve_nqueens(N)


if __name__ == "__main__":
    main()
