from constants import *
import pygame
from board import Board

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
screen.fill( BG_COLOR ) # Background Color

class Game:
    def __init__(self):
        self.board = Board()
        self.player = 1 # Player 1: 'X', Player 2: 'O'
        self.show_lines()

    def show_lines(self):
        # Vertical lines
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        # Horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)
    
    def draw_figure(self, row, col):
        if self.player == 1:
            pass # Draw X

        elif self.player == 2:
            # Draw 'O'
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2) # Create center position
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)
        

    def next_turn(self):
        self.player = self.player % 2 + 1 # Player 1: 1 % 2 = 1 + 1 = 2, or Player 2: 2 % 2 = 0 + 1 = 2