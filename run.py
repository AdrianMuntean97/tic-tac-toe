import random


def print_board(board):
    """
    Print out the game board
    """
    for row in board:
        row_str = " ".join(cell if cell != "X" 
        else "\033[32mX\033[0m" for cell in row)
        print(row_str)


def get_player_move(board):
    """
    Get input from the player and print the value provided.
    Check to see if the input provided has already been used,
    and return invalid input if the user didn't provide and integer.
    """
    while True:
        try:
            row, col = map(
                int, input("Enter row and column(example: 1 2): \n").split()
                )
            if board[row][col] == "_":
                return row, col
            else:
                print("That cell is already occupied. Please try again\n")
        except (ValueError, IndexError):
            print("Invalid input. Please try again.\n")


def get_computer_move(board):
    """
    Get a random input from the computer and print out the value
    Checks to see if the value is valid
    """
    # Check if the computer can win in the next move
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "_":
                board[row][col] = "O"
                if check_win(board) == "O":
                    board[row][col] = "_"
                    return row, col
                board[row][col] = "_"

    # Check if the player can win in the next move
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "_":
                board[row][col] = "X"
                if check_win(board) == "X":
                    board[row][col] = "_"
                    return row, col
                board[row][col] = "_"

    # Choose a random empty cell
    empty_cells = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "_":
                empty_cells.append((row, col))
    return random.choice(empty_cells)


def check_win(board):
    """
    Check each row, column and diagonal to see if the game is won
    """

    # Check rows
    for row in board:
        if set(row) == {'X'}:
            return 'X'
        elif set(row) == {'O'}:
            return 'O'

    # Check columns
    for col in range(len(board[0])):
        column = [board[row][col] for row in range(len(board))]
        if set(column) == {'X'}:
            return 'X'
        elif set(column) == {'O'}:
            return 'O'

    # Check diagonals
    diag1 = [board[i][i] for i in range(len(board))]
    diag2 = [board[i][len(board) - i - 1] for i in range(len(board))]
    if set(diag1) == {'X'}:
        return 'X'
    elif set(diag1) == {'O'}:
        return 'O'
    elif set(diag2) == {'X'}:
        return 'X'
    elif set(diag2) == {'O'}:
        return 'O'

    # No winner
    return None


def play_game():
    """
    Main function that runs the Tic-Tac-Toe game.
    Asks the player to choose the board size (3x3 to 5x5).
    Returns nothing,
    but prints out messages to the console based on game progress.
    """
    player_name = input("Enter your name: ")
    print(f"Welcome to Tic-Tac-Toe, {player_name}!\n")

    # Ask the player to choose the board size
    while True:
        board_size = input("Enter the board size (3, 4, or 5): ")
        try:
            board_size = int(board_size)
            if board_size < 3 or board_size > 5:
                print("Invalid board size. Please enter a size between 3 and 5.")
            else:
                board = [["_"] * board_size for _ in range(board_size)]
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    player_score = 0
    computer_score = 0
    current_player = "X"

    while True:
        print(f"{player_name}'s score:", player_score)
        print("Computer score:", computer_score)
        print_board(board)
        if current_player == "X":
            row, col = get_player_move(board)
        else:
            row, col = get_computer_move(board)
            print(f"The computer played at row {row + 1}, column {col + 1}")
        if board[row][col] == "_":
            board[row][col] = current_player
            winner = check_win(board)
            if winner is not None:
                print_board(board)
                if winner == "X":
                    player_score += 1
                    print(f"{player_name} wins!\n")
                else:
                    computer_score += 1
                    print("The computer wins!\n")
                board = [["_"] * len(board) for _ in range(len(board))]
                current_player = "X"
            elif all(cell != "_" for row in board for cell in row):
                print_board(board)
                print("Tie game!\n")
                board = [["_"] * len(board) for _ in range(len(board))]
                current_player = "X"
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("That cell is already occupied. Please try again.")


play_game()
