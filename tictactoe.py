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

            if event.type == pygame.KEYDOWN:
                # g key: change game mode: AI or 2 player human version (can happen mid-game)
                if event.key == pygame.K_g:
                    game.change_gamemode()

                # 0 key: change to Random AI logic
                if event.key == pygame.K_0:
                    ai.level = 0

                # 1 key: change to WTF AI logic
                if event.key == pygame.K_1:
                    ai.level = 1

                # r key: reset game
                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai

                # TODO: add a keyboard toggle for console output and/or high scores / game timer, etc
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE

                if (board.emptySquare(row, col)) and game.running:
                    game.make_move(row, col)
                    # print(board.squares) # DEBUG: print before AI makes decision

                    if game.isOver():
                        game.running = False


        if game.gameMode == 'ai' and game.player == ai.player and game.running:
            # Update the screen
            pygame.display.update()

            # AI method
            row, col = ai.eval(board)
            game.make_move(row, col)
            print(board.squares) # DEBUG: print after AI makes decision
        
        pygame.display.update()

main()