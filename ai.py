import random
from board import Board

class AI:

    def __init__(self, level = 0, player = 2):
        self.level = level
        self.player = player

    def random(self, board):
        empty_squares = board.getEmptySquares()
        index = random.randrange(0, len(empty_squares))

        return empty_squares[index] # random (row, col)

    def eval(self, main_board):
        if self.level == 0:
            # random choice
            move = self.random(main_board)
        else:
            # minimax algo
            pass

        return move # (row, col)