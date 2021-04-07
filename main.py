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

def flip_board(game_board):  # create new inverted board
    print(np.flip(game_board, 0)) # flip board, so that 0,0 is now in top left instead of bottom left

def win(game_board, game_piece):
    for c in range(col_count-3): # check if there are 4 in a row horizontally
        for r in range(row_count):
            if game_board[r][c] == game_piece and game_board[r][c+1] == game_piece and game_board[r][c+2] == game_piece and game_board[r][c+3] == game_piece: # if 4 consecutive values are the same in the same row
                return True

    for c in range(col_count): # check if there are 4 in a row vertically
        for r in range(row_count-3):
            if game_board[r][c] == game_piece and game_board[r+1][c] == game_piece and game_board[r+2][c] == game_piece and game_board[r+3][c] == game_piece: #if 4 consecutive values are the same in the same column
                return True

    for c in range(col_count-3): # check if there are 4 in a row sloped to right
        for r in range(row_count-3):
            if game_board[r][c] == game_piece and game_board[r+1][c+1] == game_piece and game_board[r+2][c+2] == game_piece and game_board[r+3][c+3] == game_piece: #if 4 consecutive values are the same on the rightward diagonal
                return True

    for c in range(col_count-3): # check if there are 4 in a row sloped to left
        for r in range(3, row_count):
            if game_board[r][c] == game_piece and game_board[r-1][c+1] == game_piece and game_board[r-2][c+2] == game_piece and game_board[r-3][c+3] == game_piece: #if all the values are the same on the leftward diagonal
                return True

game_board = c4_board()

# initializing game variables
game_is_over = False
player_turn = 1

while not game_is_over:
    #  Player A user input
    if player_turn % 2 == 1:  # If value of player turn is odd
        col_selection = int(input("Player A Please Make Your Selection (Choose Column 0-6): "))  # Ask Player A to choose row, change into a string

        if droploc_is_val(game_board, col_selection):  # If the drop location is valid (row isn't full)
            row = find_next_open_row(game_board, col_selection)  # Making row equal to the output of find_next_open_row
            drop_game_piece(game_board, row, col_selection, 1)  # Drop game piece with value 1 at specified location

            if win(game_board, 1): #if player A wins, print statement below
                print("PlAYER A IS THE CONNECT 4 CHAMP")
                game_is_over = True #end game

    # Player B user input
    else:  # If value of player turn is odd
        col_selection = int(input("Player B Please Make Your Selection (Choose Column 0-6): "))  # Ask Player B to choose row

        if droploc_is_val(game_board, col_selection):  # If the drop location is valid (row isn't full
            row = find_next_open_row(game_board, col_selection)  # If the drop location is valid (row isn't full)
            drop_game_piece(game_board, row, col_selection, 2)  # Drop game piece with value 2 at specified location

            if win(game_board, 2):
                print("PlAYER B IS THE CONNECT 4 CHAMP")
                game_is_over = True

    flip_board(game_board)

    player_turn += 1
    player_turn = player_turn % 2