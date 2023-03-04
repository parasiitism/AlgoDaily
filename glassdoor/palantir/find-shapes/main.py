"""
    1st:

    Given a black-and-white image, it is filled with 0s and 1s. It may have multiple rectangles filled with 1s and sure that every rectangle is fully filled
    The rectangles are separated by 0s. Find all the rectangles by returning the top-left and right-bottom coordinates.

    e.g.
    [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,1,1,0,0,0],
        [0,1,1,0,0,1],
        [0,1,1,0,0,1],
    ]
    Ouput: [
        [2, 1, 4, 2],
        [3, 5, 4, 5]
    ]
"""
def fill_rect(matrix, i, j, h, w):
    for di in range(h):
        for dj in range(w):
            matrix[i+di][j+dj] = 0

def f(matrix):
    R, C = len(matrix), len(matrix[0])
    res = []
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 1:
                h, w = 1, 1
                while i+h < R and matrix[i+h][j] == 1:
                    h += 1
                while j+w < C and matrix[i][j+w] == 1:
                    w += 1
                fill_rect(matrix, i, j, h, w)
                res.append((i, j, i+h-1, j+w-1))
    return res

a = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,1,1,0,0,0],
    [0,1,1,0,0,1],
    [0,1,1,0,0,1],
]
print(f(a))


"""
    2nd:
    The image has random shapes filled with 1s, separated by 0s. 
    Find all the shapes. Each shape is represented by coordinates of all the elements inside
"""

def f(matrix):
    R, C = len(matrix), len(matrix[0])

    res = []
    seen = set()
    
    def bfs(x, y):
        coordinates = []
        q = [(x, y)]
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i > R-1 or j < 0 or j > C-1:
                continue
            if matrix[i][j] != 1:
                continue
            key = (i, j)
            if key in seen:
                continue
            seen.add(key)
            coordinates.append(key)
            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))
        res.append(coordinates)

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 1 and (i, j) not in seen:
                bfs(i, j)
    
    return res

a = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,1,1,0,0,0],
    [0,1,1,0,1,1],
    [0,1,1,0,0,1],
]
print(f(a))