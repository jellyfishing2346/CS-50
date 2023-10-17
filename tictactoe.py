"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    players = 0
    turns = 0

    for index in range(len(board)):
        for count in range(len(board)):
            if board[index][count] == players:
                players += 1
            if board[index][count] == turns:
                turns += 1
        if players > turns:
            return turns
        else:
            return players


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allOutcomes = set()

    for index in range(len(board)):
        for count in range(len(board[row])):
            if board[row][count] == EMPTY:
                allOutcomes.add((index, column))
        return allOutcomes

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception('This action is not avaiable at all')
    boardCopy = copy.deepcopy(board)

    index, count = action
    boardCopy[index][count] = player(board)
    return boardCopy


def checkIndex(board, players):
    for index in range(len(board)):
        if board[index][0] == players and board[index][1] == players and board[index][2] == players:
            return True
        return False


def checkCount(board, players):
    for count in range(len(board)):
        if board[count][0] == players and board[count][1] == players and board[count][2] == players:
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
    if checkIndex(board, players) or checkCount(board, players) or topBottom(board, players) or bottomTop(board, players):
        return player
    elif checkIndex(board, turns) or checkCount(board, turns) or topBottom(board, turns) or bottomTop(board, turns):
        return turns
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == players:
        return True
    elif winner(board) == turns:
        return True

    for index in range(len(board)):
        for count in range(len(board[index])):
            if board[index][count] == EMPTY:
                return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == players:
        return 1
    elif winner(board) == turns:
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
    value = -math.inf
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
    elif player(board) == players:
        work = []
        for action in actions(board):
            work.append([minValue(result(board, action)), action])
        return sorted(plays, key=lambda index: index[0], reverse=True)[0][1]
    elif player(board) == turns:
        work = []
        for action in actions(board):
            work.append([maxValue(result(board, action)), action])
        return sorted(plays, key=lambda index: index[0], reverse=True)[0][1]
