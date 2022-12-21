import random
import copy

class AI:

    def __init__(self, level=1, player=2):
        self.level = level # level 0 = random, level 1 = Minimax AI
        self.player = player

    # Random Algo:

    def random(self, board):
        empty_squares = board.getEmptySquares()
        index = random.randrange(0, len(empty_squares))

        return empty_squares[index] # random (row, col)

    # Minimax AI Algo:

    # TODO: improve to a/B Pruning method
    def minimax(self, board, maximizing):
        
        # terminal case:
        case = board.finalState() # state is an integer 0 - 2

        # Player 1 Wins:
        if case == 1:
            return 1, None # return the evaluation & next move

        # Player 2 Wins (This is the AI player)
        if case == 2:
            return -1, None # (-1 value since AI is minimizing)
            # TODO: Make this a constant that changes with the boolean value of `maximizing`

        elif board.isFull():
            return 0, None

        if maximizing:
            max_eval = -100
            best_move = None
            empty_squares = board.getEmptySquares() # Get list of (row, col) tuples

            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board) # copy current board for next move evaluation
                temp_board.markSquare(row, col, 1)
                eval = self.minimax(temp_board, False)[0] # [0] = only return 1st value (eval)
                # Note has to be OPPOSITE the AI Players initialized value
                # TODO: Fix that with a constant that encompasses (if case == 2)
                if (eval > max_eval):
                    max_eval = eval
                    best_move = (row, col)

            return max_eval, best_move

        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_squares = board.getEmptySquares() # Get list of (row, col) tuples

            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board) # copy current board for next move evaluation
                temp_board.markSquare(row, col, self.player)
                eval = self.minimax(temp_board, True)[0] # [0] = only return 1st value (eval)
                # Note has to be OPPOSITE the AI Players initialized value
                # TODO: Fix that with a constant that encompasses (if case == 2)
                if (eval < min_eval):
                    min_eval = eval
                    best_move = (row, col)

            return min_eval, best_move

    # Minimax Eval Function:

    def eval(self, main_board):
        if self.level == 0:
            # random choice
            eval = 'random'
            move = self.random(main_board)
        else:
            # minimax algo
            eval, move = self.minimax(main_board, False) # False: AI will minimize

        print(f'AI has chosen to mark square: {move} with eval of: {eval}')

        return move # (row, col)