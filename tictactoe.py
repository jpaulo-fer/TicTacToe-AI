# Tic Tac Toe Player
import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    # Returns starting state of the board.

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    # Returns player who has the next turn on a board.

    # Variables for future comparison
    x_count = 0
    o_count = 0

    # Iteration through list of lists (board) to store moves on the "count" variables.
    for i in board:
        for j in i:
            if j == X:
                x_count += 1
            elif j == O:
                o_count += 1

    # Compares both "count" variables and decides who has the next turn, being 1 for X and 2 for O.
    if x_count == o_count:
        return 1
    elif x_count > o_count:
        return 2


def actions(board):
  
    # Returns set of all possible actions (i, j) available on the board.
  
    raise NotImplementedError


def result(board, action):

    # Returns the board that results from making move (i, j) on the board.

    raise NotImplementedError


def winner(board):

    # Returns the winner of the game, if there is one.

    raise NotImplementedError


def terminal(board):

    # Returns True if game is over, False otherwise.

    raise NotImplementedError


def utility(board):
    
    # Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    
    raise NotImplementedError


def minimax(board):

    # Returns the optimal action for the current player on the board.
    
    raise NotImplementedError
