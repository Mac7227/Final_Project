# Final_Project
Connect 4 Code

For our final project, we coded a Connect4 game. We began with coding a two person interactive game, but then replaced the second player with an AI "player". Before running the code, ensure that you import sys, numpy, pygame, math, and random.  Upon running the code, the code will ask you to input your name. Then, the code will ask you to choose a difficulty level between 'easy' 'medium' and 'hard'. The levels range from being able to beat the computer with minimal effort to extremely difficult to beat the AI (it predicts future moves and makes best possible decision using the minimax function looking up to 5 moves ahead), with medium being somewhere in between the two. For basic Connect4 players, medium will likely be the most fun, but we recommend hard for anyone looking for a challenge (Mac and none of his roommates have beaten the hard setting yet)! After typing in your name (then hitting enter) and typing in your chosen difficulty (then hitting enter), the Connect4 game will pop up in a separate window. The player who gets to place their chip first is randomized. Therefore, sometimes a green chip (AI chip) will be placed first, and sometimes a red chip will appear above the board which means it is the user's turn first. When it is the user's turn, you can move your mouse across the board and the chip will follow along the top. Then, you can click anywhere across the 7 columns to drop the chip in that column. After you place the chip, the AI will place their chip. The AI, on medium and hard settings, will make decisions that factor in the user's potential option and the AI's potential options. Therefore, it will be able to block its opponent when they have 3 in a row and will recognize moves it should make itself in order to win. The placing of the chips will continue until someone wins, at which point "_____ is the champ!!!" will flash across the top of the screen, or a tie occurs, at which point "The Game Ties!" will flash across the top of the screen. Either way, the game will end. You can then play again by running the code again. Thanks so much for a great semester and we hope you enjoy!
