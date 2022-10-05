"""
    Print all the paths in a matrix from (0,0) to (R-1, C-1) if you can only go right and down
    e.g. [
        ['A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H'],
        ['I', 'J', 'K', 'L']
    ]

    res = [
        ABCDHL,
        ABCGHL,
        ABFGHL
        ABFGKL,
        ....
        AEIJKL
    ]
"""


"""
    1st approach: DFS

    Time    ~O(2^N)     hard to determine but in the decision tree every cell has 2 directions to go
    Space   ~O(2^N)
"""


def approach1(matrix):
    R, C = len(matrix), len(matrix[0])
    res = []

    def dfs(i, j, path):
        if i < 0 or i == R or j < 0 or j == C:
            return
        path += matrix[i][j]
        if i == R-1 and j == C-1:
            res.append(path)
        else:
            dfs(i, j+1, path)
            dfs(i+1, j, path)
    dfs(0, 0, '')

    return res


m = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L']
]
print(approach1(m))

print("--end--")

"""
    2nd approach: BFS

    Time    ~O(2^N)     hard to determine but in the decision tree every cell has 2 directions to go
    Space   ~O(2^N)
"""


def approach2(matrix):
    R, C = len(matrix), len(matrix[0])
    res = []
    q = [(0, 0, '')]
    while len(q) > 0:
        i, j, path = q.pop(0)
        if i < 0 or i == R or j < 0 or j == C:
            continue
        path += matrix[i][j]
        if i == R-1 and j == C-1:
            res.append(path)
        else:
            q.append((i, j+1, path))
            q.append((i+1, j, path))

    return res


m = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L']
]
print(approach2(m))
