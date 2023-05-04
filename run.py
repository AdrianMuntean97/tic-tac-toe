import random


def print_board(board):
    """
    Print out the game board
    """
    for row in board:
        row_str = " ".join(cell if cell != "X" else "\033[32mX\033[0m" for cell in row)
        print(row_str)


def get_player_move(board):
    """
    Get input from the player and print the value provided.
    Check to see if the input provided has already been used,
    and return invalid input if the user didn't provide and integer.
    """
    while True:
        try:
            row, col = map(int, input("Enter row and column(example: 1 2): \n").split())
            if board[row][col] == "_":
                return row,col
            else:
                print("That cell is already occupied. Please try again\n")
        except (ValueError,IndexError):
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
    # check rows
    for row in range(4):
        for col in range(2):
            if board[row][col] == board[row][col+1] == board[row][col+2] != "_":
                return board[row][col]
    
    # check columns
    for col in range(4):
        for row in range(2):
            if board[row][col] == board[row+1][col] == board[row+2][col] != "_":
                return board[row][col]
    
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "_":
        return board[0][0]
    if board[1][1] == board[2][2] == board[3][3] != "_":
        return board[1][1]
    if board[0][3] == board[1][2] == board[2][1] != "_":
        return board[0][3]
    if board[1][2] == board[2][1] == board[3][0] != "_":
        return board[1][2]
    
    return None


def play_game():
    """
    Main function that runs the Tic-Tac-Toe game.
    Asks the player to choose the board size (3x3 or 4x4).
    Returns nothing, but prints out messages to the console based on game progress.
    """
    player_name = input("Enter your name: ")
    print(f"Welcome to Tic-Tac-Toe, {player_name}!\n")

    # Ask the player to choose the board size
    while True:
        board_size = input("Choose the board size (3 or 4): ")
        if board_size == "3":
            board = [["_"] * 3 for _ in range(3)]
            break
        elif board_size == "4":
            board = [["_"] * 4 for _ in range(4)]
            break
        else:
            print("Invalid input. Please enter 3 or 4.")

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
            

