# Brute Force Algorithm for Peg Solitaire

def initial(n, skip):
    """Construct triangle solitaire game with n*(n+1)/2 holes each filled
    with a peg except for a specific omitted value"""

    board = {}

    for c in range(0, 2*n, 2):
        d = 0
        for r in range((2*n-c)/2):
            board[(c+d,r)] = True
            d += 1

    if skip in board:
        board[skip] = False
    return board


def solve(board, path):
    """solve board and updates path to reflect sequence of moves"""

    if len(path) == len(board)-2:
        return True

    for move in moves(board):
        path.append(move)
        makeMove(board, move)

        if solve(board, path):
            return True

        undoMove(board, move)
        del path[-1]

    return False

# note each is a delta (c, r)
directions = [ [+4, 0], [-4, 0], [+2, +2], [+2, -2], [-2, +2], [-2, -2] ]

# move is a triple [ hole, deltac, deltar ]

def moves(board):
    """Returns possible moves given board state"""

    m = []
    for hole in board:
        if board[hole]:
            for deltac, deltar in directions:
                mid = (hole[0] + deltac/2, hole[1] + deltar/2)
                end = (hole[0] + deltac,   hole[1] + deltar)
                if mid in board and board[mid] and end in board and not board[end]:
                    m.append ([hole, deltac, deltar])

    return m
    

def makeMove(board, move):
    """Execute move on a board"""

    hole, deltac, deltar = move
    mid = (hole[0] + deltac/2, hole[1] + deltar/2)
    end = (hole[0] + deltac,   hole[1] + deltar)
    board[hole] = False
    board[mid] = False
    board[end] = True

def undoMove(board, move):
    """Execute move on a board"""

    hole, deltac, deltar = move
    mid = (hole[0] + deltac/2, hole[1] + deltar/2)
    end = (hole[0] + deltac,   hole[1] + deltar)
    board[end] = False
    board[mid] = True
    board[hole] = True


def solveSpecific(board):
    """Solve board and return path of moves"""

    path = []
    solve (board, path)
    for move in path:
        print move

