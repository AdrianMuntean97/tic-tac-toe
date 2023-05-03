import random


def print_board(board):
    """
    Print out the game board
    """
    for row in board:
        print(" ".join(row))


def get_player_move(board):
    """
    Get input from the player and print the value provided.
    Check to see if the input provided has already been used,
    and return invalid input if the user didn't provide and integer.
    """
    while True:
        try:
            row, col = map(int, input("Enter row and column(example: 1 2): ").split())
            if board[row][col] == "_":
                return row,col
            else:
                print("That cell is already occupied. Please try again")
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")


def get_computer_move(board):
    """
    Get a random input from the computer and print out the value
    Checks to see if the value is valid
    """
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == "_":
                empty_cells.append((row, col))
    return random.choice(empty_cells)


