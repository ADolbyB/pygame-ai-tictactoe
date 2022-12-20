import sys
import pygame
from game import Game

# PyGame Setup:
pygame.init()
pygame.display.set_caption("Unbeatable AI Tic Tac Toe") # Caption at top of window

def main():
    
    # Game Object
    game = Game()
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

main()