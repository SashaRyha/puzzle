"""
Tyt bude repozitoriy ssylka
"""


def rows(board: list) -> bool:
    """
    Return True if row of cells doesnt have 2 identical numbers,
    False if does.
    """
    for i in range(9):
        for j in range(9):
            try:
                if (board[i][j] != "*") and (board[i][j] != " "):
                    if board[i].count(board[i][j]) > 1:
                        return False
            except IndexError:
                continue
    return True


def cols(board: list) -> bool:
    """
    Return True if column of cells doesnt have 2 identical numbers,
    False if does.
    """
    new_board = []
    for i in range(9):
        new_colm = ""
        for j in range(9):
            new_colm += board[j][i]
        new_board += [new_colm]
    return rows(new_board)


def same_color(board: list) -> bool:
    """
    Return True if cells with same color dont have 2 identical numbers,
    False if do.
    """
    new_board2 = []
    for i in range(5):
        new_col = ""
        for j in range(4 - i, 9 - i):
            new_col += board[j][i]
        for z in range(1 + i, 5 + i):
            new_col += board[8-i][z]
        new_board2 += [new_col]
    return rows(new_board2)



def validate_board(board: list) -> bool:
    """
    Return True if functions rows, cols, same_color are True
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   9  **", "8 7  2***", "  2  ****"])
    True
    """
    if rows(board) and cols(board) and same_color(board):
        return True
    else:
        return False
