import pygame
import numpy as np
from constants import *
from ai import AI

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )

class Board:
    
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS) )
        # print(self.squares) # DEBUG: Display 2D Array of 0's in terminal
        self.empty_sqrs = self.squares
        self.marked_sqrs = 0

    def finalState(self, show=False):
        # return 0 if game not over & no winner
        # return 1 if player 1 won
        # return 2 if player 2 won
        # TODO: could make this a switch statement since default case = 0
        
        # vertical wins:
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[0][col] == 2 else X_COLOR
                    initPos = (col * SQSIZE + SQSIZE // 2, 20)
                    finPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
                    pygame.draw.line(screen, color, initPos, finPos, LINE_WIDTH)
                return self.squares[0][col] # return which player won

        # horizontal wins:
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[row][0] == 2 else X_COLOR
                    initPos = (20, row * SQSIZE + SQSIZE // 2)
                    finPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.line(screen, color, initPos, finPos, LINE_WIDTH)
                return self.squares[row][0] # return player number of winner

        # descending diagonal win:
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                    color = CIRC_COLOR if self.squares[row][0] == 2 else X_COLOR
                    initPos = (20, 20)
                    finPos = (WIDTH - 20, HEIGHT - 20)
                    pygame.draw.line(screen, color, initPos, finPos, LINE_WIDTH)
            return self.squares[1][1] # return player number who won

        # ascending diagonal win:
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                    color = CIRC_COLOR if self.squares[row][0] == 2 else X_COLOR
                    initPos = (20, HEIGHT - 20)
                    finPos = (WIDTH - 20, 20)
                    pygame.draw.line(screen, color, initPos, finPos, LINE_WIDTH)
            return self.squares[1][1] # return player number who won

        # when there is no winner yet AND game not finished: return 0
        return 0

    def markSquare(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def emptySquare(self, row, col):
        return self.squares[row][col] == 0

    def getEmptySquares(self): # Returns a list of all unmarked squares
        unmarked = []
        for row in range(ROWS):
            for col in range(COLS):
                if (self.emptySquare(row, col)):
                    unmarked.append( (row, col) )
        return unmarked

    def isFull(self):
        return self.marked_sqrs == 9

    def isEmpty(self):
        return self.marked_sqrs == 0

class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1 # Player 1: 'X', Player 2: 'O'
        self.gameMode = 'ai' #'pvp' = player vs player, 'ai' = AI player 2
        self.running = True
        self.show_lines()

    def make_move(self, row, col):
        self.board.markSquare(row, col, self.player)
        self.draw_figure(row, col)
        self.next_turn()

    def show_lines(self):
        screen.fill( BG_COLOR ) # Background Color ## FIX for game reset not refreshing
        # Vertical lines
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        # Horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)
    
    def draw_figure(self, row, col):
        if self.player == 1:
            # Draw X
            # Descending Line:
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, X_COLOR, start_desc, end_desc, X_WIDTH)
            # Ascending Line:
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, X_COLOR, start_asc, end_asc, X_WIDTH)

        elif self.player == 2:
            # Draw 'O'
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2) # Create center position
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)
        

    def next_turn(self):
        self.player = self.player % 2 + 1 # Player 1: 1 % 2 = 1 + 1 = 2, or Player 2: 2 % 2 = 0 + 1 = 2

    def change_gamemode(self):
        if self.gameMode == 'pvp':
            self.gameMode = 'ai'
        else:
            self.gameMode = 'pvp'

    def isOver(self): # true if game is over: win/tie
        return self.board.finalState(show=True) != 0 or self.board.isFull()

    def reset(self):
        self.__init__() # restart all attributes to default