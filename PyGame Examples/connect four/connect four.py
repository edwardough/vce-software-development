# import all necessary imports
import numpy as np
import pygame as pg
import sys
import math
from pygame import mixer
# defining colours
BLACK = (0,0,0)
RED = pg.Color("blue")
YELLOW = pg.Color("green")
# size of the game board
ROW_COUNT = 7
COLUMN_COUNT = 7
HEIGHT = 20
WIDTH = 20



# tutorial textbox    
def textbox():   
    pg.init()

    # size of the screen display 
    SIZE = WIDTH, HEIGHT = (1000, 600)
    FPS = 30
    screen = pg.display.set_mode(SIZE, pg.RESIZABLE)
    clock = pg.time.Clock()
    pg.display.set_caption('Tutorial')
    # creating the text box
    def blit_text(surface, text, pos, font, color=pg.Color('green')):
        words = [word.split(' ') for word in text.splitlines()]  
        space = font.size(' ')[0]  
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            #  making sure the words fall underneath each other rather than going off the screen
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  
                    y += word_height  
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  
            y += word_height  

    # the tutorial for the game, this will be displayed on the screen
    text = "So you can't play connect four?\nWhat sort of childhood did you have?\nAnyway, here's how;\n-The aim of the game is to line up four of your circles in a row, column or diagonal\n" \
        "-Taking turns with the other player, you must select a column in which to place your piece (it will drop the the bottom available space in the selected column)\n" \
        "-The game continues this way until a winner has been crowned as the connect four champion, or until the board has been completely filled, in which case you both have shown a complete lack of brain power\n" \
        "-Dont forget to be strategic and bamboozle your opponent\nHappy connect four-ing\n(close this window to begin)"
    # the font and size of the text
    font = pg.font.SysFont('Arial', 35)

    while True:

        dt = clock.tick(FPS) / 1000

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game()
                quit()
                

        screen.fill(pg.Color('black'))
        blit_text(screen, text, (20, 20), font)
        pg.display.update()
        
# creating the Connect Four game
def game():
    # creating the board out of zeros
    def create_board():
        board = np.zeros((ROW_COUNT,COLUMN_COUNT))
        return board
    # dropping pieces into the spot the player wants
    def drop_piece(board, row, col, piece):
        board[row][col] = piece
    # checking if the player has placed the piece in a valid spot
    def is_valid_location(board, col):
        return board[ROW_COUNT-1][col] == 0
    # checking where the next open spot is for the game piece
    def get_next_open_row(board, col):
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r
    # printing the board 
    def print_board(board):
        print(np.flip(board, 0))
    # checking for winning moves whether it is diagonally, horizontally, vertically
    def winning_move(board, piece):
        
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True

        
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True

        
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True

        
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True
    # using the zeros to draw the board on the screen
    def draw_board(board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pg.draw.rect(screen, pg.Color("red"), (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pg.draw.circle(screen, pg.Color("white"), (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    # drawing the game pieces 
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):		
                if board[r][c] == 1:
                    pg.draw.circle(screen, pg.Color("blue"), (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif board[r][c] == 2: 
                    pg.draw.circle(screen, pg.Color("green"), (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pg.display.update()

    # calling the boads in order for it to come up on the screen
    board = create_board()
    print_board(board)
    game_over = False
    turn = 0
    # all necassary variables
    pg.init()

    SQUARESIZE = 80

    pg.display.set_caption('Connect Four')

    width = COLUMN_COUNT * SQUARESIZE

    height = (ROW_COUNT+1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE/2 - 5)

    screen = pg.display.set_mode(size)

    draw_board(board)

    pg.display.update()

    myfont = pg.font.SysFont("monospace", 50)
    
    while not game_over:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            # detect where the mouse is moving for the ball to follow 
            if event.type == pg.MOUSEMOTION:
                pg.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pg.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                else: 
                    pg.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            pg.display.update()
            # detect when the player cliks on a certain row
            if event.type == pg.MOUSEBUTTONDOWN:
                pg.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)
                        # render when player one wins and print their name
                        if winning_move(board, 1):
                            label = myfont.render(Player1.upper() + " WINS!!", 1, RED)
                            screen.blit(label, (20,10))
                            game_over = True


                
                else:				
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))
                    # check if the piece has been placed a valid area
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)
                        # render when player two wins and print their name
                        if winning_move(board, 2):
                            label = myfont.render(Player2.upper() + " WINS!!", 1, YELLOW)
                            screen.blit(label, (20,10))
                            game_over = True
                            
                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2
                
                if game_over:
                    
                    pg.time.wait(3000)
                    celebration()
# after the game has been completed and a player has been crowned they will recieve one dogcoin
def celebration():
    global HEIGHT
    global WIDTH

    pg.init()
    mixer.init()
    screen = pg.display.set_mode((300,220), 0, 32)
    pg.display.set_caption('Prize: 1 Dogecoin')
    dogeImg = pg.image.load('dogecoin.png')
    dogex = 20
    dogey = 10
    
    # printing the dogecoin
    screen.blit(dogeImg, (dogex, dogey))
    
    # applying music with the window
    mixer.music.load("bark.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()
    running = True 
    while running:
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False


# ask for the players names and whether they know how to play the game or not
Player1 = input("Player 1 enter your name: ")
print('')
Player2 = input("Player 2 enter your name: ")
print('')
tutorial = input('''Do you know how to play connect four:
[a] no
[b] yes 
''')
if tutorial.lower() == "b":
    game()
if tutorial.lower() == "a":
    textbox() 