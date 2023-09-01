from collections import *
"""
    1st: 
    
    Given a matrix with 0 is crossible cell and -1 is a wall, and give you an start_position (where must be a crossible cell), 
    determine if we can visit all the crossible cells

    e.g.1
    matrix = [
        [-1, 0, 0, 0, 0],
        [0, 0, -1, -1, 0],
        [0, -1, 0, 0, 0],
        [0, -1, 0, -1, 0],
        [0, 0, 0, -1, 0],
    ], start_position = (0, 1)

    output: True

    e.g.2
    matrix =[
        [-1, 0, 0, 0, 0],
        [0, 0, -1, -1, 0],
        [0, -1, 0, -1, 0],
        [0, -1, -1, -1, 0],
        [0, 0, 0, -1, 0],
    ], start_position = (0, 1)

    output: False
"""
def f(matrix, start_position):
    R, C = len(matrix), len(matrix[0])
    q = [start_position]
    while len(q) > 0:
        i, j = q.pop(0)
        if i < 0 or i > R-1 or j < 0 or j > C-1:
            continue
        if matrix[i][j] != 0:
            continue
        matrix[i][j] = -1
        for di,dj in [(-1, 0), (1, 0), (0,-1), (0,1)]:
            q.append((i+di, j+dj))
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                return False
    return True

a =[
    [-1, 0, 0, 0, 0],
    [0, 0, -1, -1, 0],
    [0, -1, 0, 0, 0],
    [0, -1, 0, -1, 0],
    [0, 0, 0, -1, 0],
]
b = (0, 1)
print(f(a, b))

a =[
    [-1, 0, 0, 0, 0],
    [0, 0, -1, -1, 0],
    [0, -1, 0, -1, 0],
    [0, -1, -1, -1, 0],
    [0, 0, 0, -1, 0],
]
b = (0, 1)
print(f(a, b))

"""
    2nd:
    
    Given a matrix with 0 is crossible cell, -1 is a wall and 1 is a diamond, and give you an start_position (where must be a crossible cell), 
    return the short path(s) to all the diamonds

    e.g.1
    matrix = [
        [0,  0,  0,  0, 0, 0],
        [0, -1, -1, -1, 0, 0],
        [0, -1, -1, -1, 1, 1],
        [0, -1, -1, -1, 0, 0],
        [0,  0,  0,  0, 0, 0],
    ], start_position = (2,0)

    Output: [
        [(2,0),(1,0),(0,0),(0,1),(0,2),(0,3),(0,4),(1,4),(2,4),(2,5)],
        [(2,0),(3,0),(4,0),(4,1),(4,2),(4,3),(4,4),(3,4),(2,4),(2,5)],
    ]
"""
def f(matrix, start_position):
    R, C = len(matrix), len(matrix[0])
    diamonds = 0
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 1:
                diamonds += 1
    res = []
    def backtracking(i, j, path, maining_diamonds):
        nonlocal res
        if i < 0 or i > R-1 or j < 0 or j > C-1:
            return
        if matrix[i][j] == -1 or matrix[i][j] == 99:
            return
        if matrix[i][j] == 1:
            maining_diamonds -= 1
        
        new_path = path + [(i, j)]

        # optimization
        if len(res) > 0 and len(new_path) > len(res[-1]):
            return
        
        # put new_path in res, and prune the paths in result if the len(new_path) < any paths' length in result
        if maining_diamonds == 0:
            if len(res) == 0:
                res.append(new_path)
            else:
                if len(new_path) < len(res[-1]):
                    res = [new_path]
                elif len(new_path) == len(res[-1]):
                    res.append(new_path)
            return
        
        orig = matrix[i][j]
        matrix[i][j] = 99
        backtracking(i-1, j, new_path, maining_diamonds)
        backtracking(i+1, j, new_path, maining_diamonds)
        backtracking(i, j-1, new_path, maining_diamonds)
        backtracking(i, j+1, new_path, maining_diamonds)
        matrix[i][j] = orig
        return
    
    backtracking(start_position[0], start_position[1], [], diamonds)

    return res


a = [
    [0,  0,  0,  0, 0, 0],
    [0, -1, -1, -1, 0, 0],
    [0, -1, -1, -1,  1, 1],
    [0, -1, -1, -1, 0, 0],
    [0,  0,  0,  0, 0, 0],
]
b = (2,0)
print(f(a, b))