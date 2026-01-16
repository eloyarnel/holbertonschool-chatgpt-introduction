#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Check diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False


def board_full(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                return False
    return True


def get_valid_index(prompt):
    while True:
        value = input(prompt).strip()

        # Validate numeric input (also rejects empty string)
        if not value.isdigit():
            print("Invalid input. Please enter 0, 1, or 2.")
            continue

        num = int(value)

        # Validate range
        if num < 0 or num > 2:
            print("Out of range. Please enter 0, 1, or 2.")
            continue

        return num


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Stop if draw
        if board_full(board):
            print("It's a draw!")
            return

        row = get_valid_index("Enter row (0, 1, or 2) for player " + player + ": ")
        col = get_valid_index("Enter column (0, 1, or 2) for player " + player + ": ")

        # Validate empty spot
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place move
        board[row][col] = player

        # Check win BEFORE switching player (fixes wrong winner bug)
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            return

        # Switch player
        player = "O" if player == "X" else "X"


tic_tac_toe()

