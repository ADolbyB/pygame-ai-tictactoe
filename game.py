from constants import *
import pygame
from board import Board
from ai import AI

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )

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
        return self.board.finalState() != 0 or self.board.isFull()

    def reset(self):
        self.__init__() # restart all attributes to default