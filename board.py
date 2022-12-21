from constants import *
import numpy as np

class Board:
    
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS) )
        # print(self.squares) # DEBUG: Display 2D Array of 0's in terminal
        self.empty_sqrs = self.squares
        self.marked_sqrs = 0

    def finalState(self):
        # TODO: could make this a switch statement since default case = 0
        # return 0 if game not over & no winner
        # return 1 if player 1 won
        # return 2 if player 2 won
        
        # vertical wins:
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                return self.squares[0][col] # return which player won

        # vertical wins:
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                return self.squares[row][0] # return player number of winner

        # descending diagonal win:
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            return self.squares[1][1] # return player number who won

        # ascending diagonal win:
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            return self.squares[1][1] # return player number who won

        # when there is no winner yet AND game not finished: return 0
        return 0

    def markSquare(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def emptySquare(self, row, col):
        return self.squares[row][col] == 0

    def getEmptySquares(self): # Returns a list of all unmarked squares
        unmarked = []
        for row in range(ROWS):
            for col in range(COLS):
                if (self.emptySquare(row, col)):
                    unmarked.append( (row, col) )
        return unmarked

    def isFull(self):
        return self.marked_sqrs == 9

    def isEmpty(self):
        return self.marked_sqrs == 0