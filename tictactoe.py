import sys
import pygame
from constants import SQSIZE
from game import Game

# PyGame Setup:
pygame.init()
pygame.display.set_caption("WTF AI Tic Tac Toe") # Caption at top of window

def main():
    
    # Game Object
    game = Game()
    board = game.board # refactor for simplification
    ai = game.ai
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE

                if (board.emptySquare(row, col)):
                    game.make_move(row, col)
                    # print(board.squares) # DEBUG: print before AI makes decision

        if game.gameMode == 'ai' and game.player == ai.player:
            # Update the screen
            pygame.display.update()

            # AI method
            row, col = ai.eval(board)
            game.make_move(row, col)
            print(board.squares) # DEBUG: print after AI makes decision
        
        pygame.display.update()

main()