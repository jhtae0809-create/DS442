############################################################
# CMPSC/DS 442: Homework 3 
############################################################

student_name = "Hyuntae Jeong"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import random

############################################################
# Section 1: Dominoes Game
############################################################

def make_dominoes_game(rows, cols):
    return DominoesGame([[False]*cols for _ in range(rows)])

class DominoesGame(object):

    # Required
    def __init__(self, board):
        self.__board = board
        self.__m = len(board)
        self.__n = len(board[0])

    def get_board(self):
        return self.__board

    def reset(self):
        self.__board = make_dominoes_game(self.__m, self.__n).get_board()

    def is_legal_move(self, row, col, vertical):
        if vertical:
            if row < self.__m -1 and row >= 0 and col < self.__n and col >= 0:
                if not self.__board[row][col] and not self.__board[row+1][col]:
                    return True
        else:
            if row < self.__m and row >= 0 and col < self.__n - 1 and col >= 0:
                if not self.__board[row][col] and not self.__board[row][col+1]:
                    return True
        return False
        
    def legal_moves(self, vertical):
        for i in range(self.__m):
            for j in range(self.__n):
                if self.is_legal_move(self, i, j, vertical):
                    yield (i,j)

    def execute_move(self, row, col, vertical):
        #if is_legal_move
        self.__board[row][col]=True
        if vertical:
            self.__board[row+1][col]=True
        else:
            self.__board[row][col+1]=True

    def game_over(self, vertical):
        return len(self.legal_moves(vertical)) == 0

    def copy(self):
        return DominoesGame(self.__board)

    def successors(self, vertical):
        for i, j in self.legal_moves(vertical):
            yield (i, j), self.copy().execute_move(i,j, vertical)

    def get_random_move(self, vertical):
        return random.choice(self.legal_moves(vertical))

    # Required
    def get_best_move(self, limit, vertical):
        pass


############################################################
# Section 2: Sudoku
############################################################

def sudoku_cells():
    pass

def sudoku_arcs():
    pass

def read_board(path):
    pass

class Sudoku(object):

    CELLS = sudoku_cells()
    ARCS = sudoku_arcs()

    def __init__(self, board):
        pass

    def get_values(self, cell):
        pass

    def remove_inconsistent_values(self, cell1, cell2):
        pass

    def infer_ac3(self):
        pass

    def infer_improved(self):
        pass

    def infer_with_guessing(self):
        pass

