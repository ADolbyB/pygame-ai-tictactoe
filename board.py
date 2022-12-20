from constants import *
import numpy as np

class Board:
    
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS) )
        # print(self.squares) # DEBUG: Display 2D Array of 0's in terminal

    def mark_square(self, row, col, player):
        self.squares[row][col] = player

    def empty_square(self, row, col):
        return self.squares[row][col] == 0