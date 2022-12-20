from constants import *
import numpy as np

class Board:
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS) )
        # print(self.squares) # DEBUG: Display in terminal