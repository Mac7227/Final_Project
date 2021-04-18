import sys
import numpy as np
import pygame
import math
import random

Brown = (139,69,19) # sets color brown for use in visual board
White = (255,255,255) # sets color white for use in visual board
Red = (255,0,0) # sets color red for use in visual board
Yellow = (204,204,0) # sets color yellow for use in visual board

# initialize board dimensions
row_count = 6
col_count = 7

# initialize players of game
PlayerA = 1
AI = 0

# initialize pieces for each player
PlayerA_piece = 1
AI_piece = 2
empty = 0

# initializes the goal for the AI to make decisions off of
block_len = 4


PlayerA_name_response = str(input("What is your name?")) # Gets name of User to Customize Win Announcement if they Win



# Create matrix of zeros to initialize game board
def c4_board(row_count, col_count):
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


def easy(block, game_piece): ## Establishes easy scoring mechanism for AI to base decisions off of
    score = 0
    opponent_piece = PlayerA_piece
    if game_piece == PlayerA_piece:
        opponent_piece = AI_piece

    if block.count(game_piece) == 4:
        score += 50
    elif block.count(game_piece) == 3 and block.count(empty) == 1:
        score += 55
    elif block.count(game_piece) == 2 and block.count(empty) == 2:
        score += 60
    if block.count(opponent_piece) == 3 and block.count(empty) == 1:
        score -= 5
    elif block.count(opponent_piece) == 4:
        score -= 10
    return score

def medium(block, game_piece): ## Establishes medium scoring mechanism for AI to base decisions off of
    score = 0
    opponent_piece = PlayerA_piece
    if game_piece == PlayerA_piece:
        opponent_piece = AI_piece

    if block.count(game_piece) == 4:
        score += 245
    elif block.count(game_piece) == 3 and block.count(empty) == 1:
        score += 115
    elif block.count(game_piece) == 2 and block.count(empty) == 2:
        score += 25
    if block.count(opponent_piece) == 3 and block.count(empty) == 1:
        score -= 150
    elif block.count(opponent_piece) == 4:
        score -= 225
    return score

def hard(block, game_piece): #Establishes hard base of scoring mechanism that minimax function uses
    score = 0
    opponent_piece = PlayerA_piece
    if game_piece == PlayerA_piece:
        opponent_piece = AI_piece

    if block.count(game_piece) == 4:
        score += 100
    elif block.count(game_piece) == 3 and block.count(empty) == 1:
        score += 15
    elif block.count(game_piece) == 2 and block.count(empty) == 2:
        score += 5
    if block.count(opponent_piece) == 3 and block.count(empty) == 1:
        score -= 35
    return score

while True: # Asks user what level of difficulty they want to play the AI at
    difficulty_choice = input("Choose Difficulty level 'Type: 'easy' 'medium' or 'hard'")
    if difficulty_choice in locals() and callable(locals()[difficulty_choice]):
        difficulty_choice = locals()[difficulty_choice]
        break
    else:
        print('Not valid response, try again')


def score_pos(game_board, game_piece): # Scoring based on positioning in cooperation with the different scoring difficulties above
    score = 0

    center_array = [int(ii) for ii in list(game_board[:, col_count // 2])] ## this chunk tells the AI to put more importance on the middle of the board to place its pieces
    center_count = center_array.count(game_piece)
    score += center_count * 4

    for r in range(row_count): # Horizontal score for AI loop
        row_array = [int(ii) for ii in list(game_board[r, :])] # indexing specific row and all its columnns
        for c in range(col_count - 3):
            block = row_array[c:c + block_len]
            score += difficulty_choice(block, game_piece)

    for c in range(col_count): # Vertical score for AI loop
        col_array = [int(ii) for ii in list(game_board[:,c])] ## indexing specific columns and all of its rows
        for r in range(row_count - 3):
            block = col_array[r:r + block_len]
            score += difficulty_choice(block, game_piece)

    for r in range(row_count -3): # Diagonals sloped up to the right score for AI loop
        for c in range(col_count-3):
            block = [game_board[r+ii][c+ii] for ii in range(block_len)] # sets block to all diagonals sloped up to the right
            score += difficulty_choice(block, game_piece)

    for r in range(row_count-3): # Diagonals sloped downward to the right score for AI loop
        for c in range(col_count-3):
            block = [game_board[r+3-ii][c+ii] for ii in range(block_len)]
            score += difficulty_choice(block, game_piece)
    return score

def game_is_done(game_board): # Function that returns possible situations of game being over as boolean variables for minimax
    return win(game_board, PlayerA_piece) or win(game_board, AI_piece) or len(get_val_loc(game_board)) == 0

def minimax(game_board, depth, alpha, beta, maximizingplayer): # minimax function that allows AI to choose best move based on future possible moves
    val_loc = get_val_loc(game_board)
    game_done = game_is_done(game_board)
    if depth == 0 or game_done: # Determines if game is done
        if game_done:
            if win(game_board, AI_piece):
                return (None, 1000000000000)
            elif win(game_board, PlayerA_piece):
                return (None, -1000000000000)
            else:
                return (None, 0)
        else:
            return(None, score_pos(game_board, AI_piece))
    if maximizingplayer: # Code that determines location for highest possible score for AI
        value = -math.inf
        column = random.choice(val_loc)
        for col_selection in val_loc:
            row = find_next_open_row(game_board, col_selection)
            game_board_copy = game_board.copy()
            drop_game_piece(game_board_copy, row, col_selection, AI_piece)
            new_score = minimax(game_board_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col_selection
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else: # Code that determines location for lowest possible score for opponent of AI
        value = math.inf
        column = random.choice(val_loc)
        for col_selection in val_loc:
            row = find_next_open_row(game_board, col_selection)
            game_board_copy = game_board.copy()
            drop_game_piece(game_board_copy, row, col_selection, PlayerA_piece)
            new_score = minimax(game_board_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col_selection
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value # This function compares the effects of different possible moves for both the AI and user
                             # then it chooses the best location to maximize AI score and minimize user score




def get_val_loc(game_board): # determine whether or not the column choice is valid and open
    val_loc = []
    for col_selection in range(col_count):
        if droploc_is_val(game_board, col_selection):
            val_loc.append(col_selection)
    return val_loc

def best_move(game_board, game_piece): # determine what the next best move is
    val_loc = get_val_loc(game_board)
    best_score = -10000
    best_col_selection = random.choice(val_loc)
    for col_selection in val_loc:
        row = find_next_open_row(game_board, col_selection)
        new_board = game_board.copy() #create new memory location
        drop_game_piece(new_board, row, col_selection, game_piece) #pass new memory location into our drop function
        score = score_pos(new_board, game_piece) #find score of new board
        if score > best_score: #keep track of score
            best_score = score
            best_col_selection = col_selection
    return best_col_selection


def draw_board(game_board): # function to draw game board with set sizes based on for loops with c and r
    for c in range(col_count):
        for r in range(row_count):
            pygame.draw.rect(screen, Brown, (c*square_size, r*square_size+square_size, square_size, square_size)) # draws the rectangular portion of the game board
            pygame.draw.circle(screen, White, (int(c*square_size+square_size/2), int(r*square_size+square_size+square_size/2)), radius) # draws the circular portion of the game board
    for c in range(col_count):  # nested for loop that checks every spot on board to see if a piece is present
        for r in range(row_count):
            if game_board[r][c] == PlayerA_piece:  # if player A has a piece in a certain spot, draw a red circle in that spot
                pygame.draw.circle(screen, Red, (int(c * square_size + square_size / 2), height-int(r * square_size + square_size / 2)), radius)
            elif game_board[r][c] == AI_piece:  # if player B has a piece in a certain spot, draw a yellow circle in that spot
                pygame.draw.circle(screen, Yellow, (int(c * square_size + square_size / 2), height-int(r * square_size + square_size / 2)), radius)
    pygame.display.update()  # once circles are drawn, update game board


game_board = c4_board(row_count, col_count)

# initializing game variables
game_is_over = False

pygame.init()

square_size = 100  # Sets size of squares for visual board

width = col_count * square_size  # sets the width for the visual board to size of square by number of columns
height = (row_count + 1) * square_size  # sets the height of visual to size of square by number of rows plus 1

size = (width, height)  # sets variable equal to the height and width of the visual board
radius = int(square_size/2 - 5) # sets radius for circles in visual board

screen = pygame.display.set_mode(size)  # displays the visual board
draw_board(game_board)  # draws the board with new visual attributes from line 61
pygame.display.update()  # updates the game board to new visual attributes

Win_Font = pygame.font.SysFont("Times", 50)

player_turn = random.randint(AI, PlayerA) # randomize who goes first

while not game_is_over:  # while the game is not over, continues loop

    for event in pygame.event.get():  # initializes the different events that will be looked for in game
        if event.type == pygame.QUIT:  # allows user to quit the game by using exit button
            sys.exit()
        if event.type == pygame.MOUSEMOTION:  # creates function that has the piece follow the mouse along the top rect
            pygame.draw.rect(screen, White, (0,0,width,square_size))  # draws white rectangle so that only one copy of piece appears
            posx = event.pos[0]
            if player_turn == PlayerA:  # if it is player A's turn, red piece
                pygame.draw.circle(screen, Red, (posx, int(square_size/2)), radius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN: ## initializes the type of event (clicking mouse) to make changes in game
            pygame.draw.rect(screen, White, (0, 0, width, square_size))
            # print(event.pos)
            # Player A user input
            if player_turn == PlayerA:  # If value of player turn is odd
                posx = event.pos[0]    # initializes the click of player to x position of click
                col_selection = int(math.floor(posx/square_size)) # sets clicks to align with the set columns

                if droploc_is_val(game_board, col_selection):  # If the drop location is valid (row isn't full)
                    row = find_next_open_row(game_board,
                                             col_selection)  # Making row equal to the output of find_next_open_row
                    drop_game_piece(game_board, row, col_selection, PlayerA_piece)  # Drop game piece with value 1 at specified location

                    if win(game_board, PlayerA_piece):  # if player A wins, print win statement at top of game board in red color
                        win_label = Win_Font.render(PlayerA_name_response + " IS THE CHAMP",1,Red)  # create win label in red
                        screen.blit(win_label, (35,10))  # print win label at top of board
                        game_is_over = True  # end game

                    if len(get_val_loc(game_board)) == 0: # Ends game if tie
                        win_label = Win_Font.render('The Game Ties!', 1,Brown)
                        screen.blit(win_label, (35, 10))
                        game_is_over = True

                    # once AI turn is completed, update turn
                    player_turn += 1
                    player_turn = player_turn % 2

                    # flip and then draw the game board after each turn to update
                    flip_board(game_board)
                    draw_board(game_board)

            # AI user input
        if player_turn == AI and not game_is_over: # initialize AI
            if difficulty_choice == easy or difficulty_choice == medium: # Chooses the set of rules / scoring to follow dependent upon user input
                col_selection = best_move(game_board, AI_piece)
            elif difficulty_choice == hard:
                col_selection, minimax_score = minimax(game_board, 5, -math.inf, math.inf, True)

            if droploc_is_val(game_board, col_selection):  # If the drop location is valid (row isn't full)
                pygame.time.wait(500) # wait 0.5seconds to place AI chip
                row = find_next_open_row(game_board, col_selection)  # If the drop location is valid (row isn't full)
                drop_game_piece(game_board, row, col_selection, AI_piece)  # Drop game piece with value 2 at specified location

                if win(game_board, AI_piece):  # if player B wins print win statement at top of game board
                    win_label = Win_Font.render("COMPUTER IS THE CHAMP", 1, Yellow)  # create win label in yellow
                    screen.blit(win_label, (35, 10))  # print win label at top of board
                    game_is_over = True  # end game once player wins

                if len(get_val_loc(game_board)) == 0:  # Ends game if tie
                    win_label = Win_Font.render('The Game Ties!', 1, Brown)
                    screen.blit(win_label, (35, 10))
                    game_is_over = True

                # flip and then draw the game board after each turn to update
                flip_board(game_board)
                draw_board(game_board)

                # once a players turn is completed, update turn
                player_turn += 1
                player_turn = player_turn % 2



    if game_is_over:  # when game ends, wait 3 seconds so that players can read the win statement
        pygame.time.wait(3000)
