import numpy as np

# Creating dimensions for game board
row_count = 6
col_count = 7


# Create matrix of zeros to initialize game board
def c4_board():
    game_board = np.zeros((row_count, col_count))
    return game_board


# Dropping game piece at user inputted location
def drop_game_piece(game_board, row, col_selection, game_piece):
    game_board[row][col_selection] = game_piece     # Makes the game piece (1 for player A and 2 for player B)
                                                    # go to user selected column and next available row


# Checking if user inputted drop location is a valid location (doesn't contain another piece)
def droploc_is_val(game_board, col_selection):
    return game_board[row_count - 1][col_selection] == 0  # checking to see that the drop location is empty


# Finding the next open row where the piece should be dropped
def find_next_open_row(game_board, col_selection):
    for r in range(row_count):  # loops through all possible rows
        if game_board[r][col_selection] == 0:  # if r row is empty
            return r  # End loop/function and return the the value of the next empty row as r


game_board = c4_board()
print_board(game_board)
def print_board(game_board):
    print(np.flip(game_board, 0)
    return

game_is_over = False
player_turn = 0

while game_is_over == 0:
    print(game_board)
    #  Player A user input
    if player_turn % 2 == 1:  # If value of player turn is odd
        col_selection = input("Player A Please Make Your Selection (Choose Column 0-6): ")  # Ask Player A to choose row

        if droploc_is_val(game_board, col_selection):  # If the drop location is valid (row isn't full)
            row = find_next_open_row(game_board, col_selection)  # Making row equal to the output of find_next_open_row
            drop_game_piece(game_board, row, col_selection, 1)  # Drop game piece with value 1 at specified location
    # Player B user input
    else:  # If value of player turn is odd
        col_selection = input("Player B Please Make Your Selection (Choose Column 0-6): ")  # Ask Player B to choose row

        if droploc_is_val(game_board, col_selection):  # If the drop location is valid (row isn't full
            row = find_next_open_row(game_board, col_selection)  # If the drop location is valid (row isn't full
            drop_game_piece(game_board, row, col_selection, 2)  # Drop game piece with value 2 at specified location

    print(game_board) # Shows user the current status of the game board

    player_turn += 1 # Changes the round of turns to the next round
