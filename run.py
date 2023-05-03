import random


def print_board(board):
    """
    Print out the game board
    """
    for row in board:
        print(" ".join(row))