from constants import *
import pygame
from board import Board

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
screen.fill( BG_COLOR ) # Background Color

class Game:
    def __init__(self):
        self.board = Board()
        self.show_lines()

    def show_lines(self):
        # Vertical lines
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        # Horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)