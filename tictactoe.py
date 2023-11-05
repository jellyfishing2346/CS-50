"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counter = 0
    for row in board:
       for cell in row:
          if cell is not EMPTY:  # assuming EMPTY is a constant defined elsewhere
             counter += 1
    return X if counter % 2 == 0 else O  # assuming X and O are constants defined elsewhere



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allOutcomes = set()
    row = 0
    column = 0

    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == EMPTY:
                allOutcomes.add((row, column))
    # return should be here, outside of the loops
    return allOutcomes


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if tuple(action) not in actions(board):
        raise Exception("This action is not avaiable at all")
    boardCopy = copy.deepcopy(board)

    index, count = action
    boardCopy[index][count] = player(board)
    return boardCopy


def checkIndex(board, players):
    for index in range(len(board)):
        if (
            board[index][0] == players
            and board[index][1] == players
            and board[index][2] == players
        ):
            return True
    return False


def checkCount(board, players):
    for count in range(len(board)):
        if (
            board[count][0] == players
            and board[count][1] == players
            and board[count][2] == players
        ):
            return True
    return False


def topBottom(board, players):
    counting = 0
    for index in range(len(board)):
        for count in range(len(board)):
            if index == count and board[index][len(board) - index - 1] == players:
                counting += 1
    return counting == 3


def bottomTop(board, players):
    counting = 0
    for index in range(len(board)):
        for count in range(len(board)):
            if index == count and board[index][count] == players:
                counting += 1
    return counting == 3


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (
        checkIndex(board, 'X')
        or checkCount(board, 'X')
        or topBottom(board, 'X')
        or bottomTop(board, 'X')
    ):
        return 'X'
    elif (
        checkIndex(board, 'O')
        or checkCount(board, 'O')
        or topBottom(board, 'O')
        or bottomTop(board, 'O')
    ):
        return 'O'
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    winnerFound = winner(board)
    if winnerFound != None:
        return True
    for r in board:
        if EMPTY in r:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def maxValue(board):
    value = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        value = max(value, minValue(result(board, action)))
    return value


def minValue(board):
    value = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        value = min(value, maxValue(result(board, action)))
    return value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    players = player(board)
    work = []
    for action in actions(board):
        if players == player(board):
            work.append([minValue(result(board, action)), action])
        else:
            work.append([maxValue(result(board, action)), action])
    if players == player(board):
        return max(work, key=lambda numIndex: numIndex[0])[1]
    else:
        return min(work, key=lambda numIndex: numIndex[0])[1]

