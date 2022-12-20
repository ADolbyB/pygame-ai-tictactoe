import sys
import pygame
from constants import SQSIZE
from game import Game

# PyGame Setup:
pygame.init()
pygame.display.set_caption("Unbeatable AI Tic Tac Toe") # Caption at top of window

def main():
    
    # Game Object
    game = Game()
    board = game.board # refactor for simplification
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE

                if (board.empty_square(row, col)):
                    board.mark_square(row, col, game.player)
                    game.draw_figure(row, col)
                    game.next_turn()
                    print(board.squares) # DEBUG

        pygame.display.update()

main()