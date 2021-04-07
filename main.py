import sys
import numpy as np
import pygame
import math

Yellow = (255,255,0) # sets color yellow for use in visual board
Black = (0,0,0) # sets color black for use in visual board

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

def draw_board(game_board): # function to draw game board with set sizes based on for loops with c and r
    for c in range(col_count):
        for r in range(row_count):
            pygame.draw.rect(screen, Yellow, (c*square_size, r*square_size+square_size, square_size, square_size)) # draws the rectangular portion of the game board
            pygame.draw.circle(screen, Black, (int(c*square_size+square_size/2), int(r*square_size+square_size+square_size/2)), radius) # draws the circular portion of the game board


game_board = c4_board()

# initializing game variables
game_is_over = False
player_turn = 1
turn = 0

pygame.init()

square_size = 100 ## Sets size of squares for visual board

width = col_count * square_size ## sets the width for the visual board to size of square by number of columns
height = (row_count + 1) * square_size ## sets the height of visual to size of square by number of rows plus 1

size = (width, height) ## sets variable equal to the height and width of the visual board
radius = int(square_size/2 - 5) # sets radius for circles in visual board

screen = pygame.display.set_mode(size) ## displays the visual board
draw_board(game_board) ## draws the board with new visual attributes from line 61
pygame.display.update() ## updates the game board to new visual attributes

while not game_is_over: ## while the game is not over, continues loop

    for event in pygame.event.get(): ## initializes the different events that will be looked for in game
        if event.type == pygame.QUIT: ## allows user to quit the game by using exit button
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: ## initializes the type of event (clicking mouse) to make changes in game
            # print(event.pos)
            # Player A user input
            if player_turn % 2 == 1:  # If value of player turn is odd
                posx = event.pos[0]    # initializes the click of player to x position of click
                col_selection = int(math.floor(posx/square_size)) # sets clicks to align with the set columns

                if droploc_is_val(game_board, col_selection):  # If the drop location is valid (row isn't full)
                    row = find_next_open_row(game_board,
                                             col_selection)  # Making row equal to the output of find_next_open_row
                    drop_game_piece(game_board, row, col_selection,
                                    1)  # Drop game piece with value 1 at specified location

                    if win(game_board, 1):  # if player A wins, print statement below
                        print("PlAYER A IS THE CONNECT 4 CHAMP")
                        game_is_over = True  # end game

            # Player B user input
            else:  # If value of player turn is odd
                posx = event.pos[0]  # initializes the click of player to x position of click
                col_selection = int(math.floor(posx / square_size))  # sets clicks to align with the set columns

                if droploc_is_val(game_board, col_selection):  # If the drop location is valid (row isn't full
                    row = find_next_open_row(game_board,
                                             col_selection)  # If the drop location is valid (row isn't full)
                    drop_game_piece(game_board, row, col_selection,
                                    2)  # Drop game piece with value 2 at specified location

                    if win(game_board, 2):
                        print("PlAYER B IS THE CONNECT 4 CHAMP")
                        game_is_over = True

            flip_board(game_board)

            player_turn += 1
            player_turn = player_turn % 2

