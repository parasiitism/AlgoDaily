from collections import *
"""
    https://www.youtube.com/watch?v=zisu0Qf4TAI
    
    A nonogram is a logic puzzle, similar to a crossword, in which the player is given a blank grid and has to color it according to some instructions. 
    Specifically, each cell can be either black or white, which we will represent as 0 for black and 1 for white.

    +------------+
    | 1  1  1  1 |
    | 0  1  1  1 |
    | 0  1  0  0 |
    | 1  1  0  1 |
    | 0  0  1  1 |
    +------------+

    For each row and column, the instructions give the lengths of contiguous runs of black (0) cells. 
    For example, the instructions for one row of [ 2, 1 ] indicate that there must be a run of two black cells, followed later by another run of one black cell, and the rest of the row filled with white cells.

    These are valid solutions: [ 1, 0, 0, 1, 0 ] and [ 0, 0, 1, 1, 0 ] and also [ 0, 0, 1, 0, 1 ]
    This is not valid: [ 1, 0, 1, 0, 0 ] since the runs are not in the correct order.
    This is not valid: [ 1, 0, 0, 0, 1 ] since the two runs of 0s are not separated by 1s.

    Your job is to write a function to validate a possible solution against a set of instructions. 
    Given a 2D matrix representing a player's solution; 
    and instructions for each row along with additional instructions for each column; 
    return True or False according to whether both sets of instructions match.

    Example instructions #1

    matrix1 = [
        [1,1,1,1],
        [0,1,1,1],
        [0,1,0,0],
        [1,1,0,1],
        [0,0,1,1]
    ]
    rows1_1    =  [], [1], [1,2], [1], [2]
    columns1_1 =  [2,1], [1], [2], [1]
    validateNonogram(matrix1, rows1_1, columns1_1) => True

    Example solution matrix:
    matrix1 ->
                                    row
                    +------------+     instructions
                    | 1  1  1  1 | <-- []
                    | 0  1  1  1 | <-- [1]
                    | 0  1  0  0 | <-- [1,2]
                    | 1  1  0  1 | <-- [1]
                    | 0  0  1  1 | <-- [2]
                    +------------+
                    ^  ^  ^  ^
                    |  |  |  |
    column       [2,1] | [2] |
    instructions      [1]   [1]


    Example instructions #2

    (same matrix as above)
    rows1_2    =  [], [], [1], [1], [1,1]
    columns1_2 =  [2], [1], [2], [1]
    validateNonogram(matrix1, rows1_2, columns1_2) => False

    The second and third rows and the first column do not match their respective instructions.

    Example instructions #3

    matrix2 = [
        [ 1, 1 ],
        [ 0, 0 ],
        [ 0, 0 ],
        [ 1, 0 ]
    ]
    rows2_1    = [], [2], [2], [1]
    columns2_1 = [1, 1], [3]
    validateNonogram(matrix2, rows2_1, columns2_1) => False

    The black cells in the first column are not separated by white cells.

    n: number of rows in the matrix
    m: number of columns in the matrix
"""
def validateNonogram(matrix, row_intructions, column_intructions):
    R, C = len(matrix), len(matrix[0])
    rowZeroCount = defaultdict(list)
    columZeroCount = defaultdict(list)
    for i in range(R):
        cnt = 0
        for j in range(C):
            if matrix[i][j] == 0:
                cnt += 1
            else:
                if cnt > 0: 
                    rowZeroCount[i].append(cnt)
                cnt = 0
        if cnt > 0:
            rowZeroCount[i].append(cnt)
    for j in range(C):
        cnt = 0
        for i in range(R):
            if matrix[i][j] == 0:
                cnt += 1
            else:
                if cnt > 0: 
                    columZeroCount[j].append(cnt)
                cnt = 0
        if cnt > 0:
            columZeroCount[j].append(cnt)
    # check
    for i in range(R):
        if tuple(row_intructions[i]) != tuple(rowZeroCount[i]):
            return False
    for j in range(C):
        if tuple(column_intructions[j]) != tuple(columZeroCount[j]):
            return False
    return True

a = [
    [1,1,1,1],
    [0,1,1,1],
    [0,1,0,0],
    [1,1,0,1],
    [0,0,1,1]
]
b = [[], [1], [1,2], [1], [2]]
c = [[2,1], [1], [2], [1]]
print(validateNonogram(a, b, c))

a = [
    [ 1, 1 ],
    [ 0, 0 ],
    [ 0, 0 ],
    [ 1, 0 ]
]
b = [[], [2], [2], [1]]
c = [[1, 1], [3]]
print(validateNonogram(a, b, c))