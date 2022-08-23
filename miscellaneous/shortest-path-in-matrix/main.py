from email.policy import default
from collections import *
"""
    1st: find the short path, from top-left to bottom-right in a matrx
    - in the matrix, 1 means a roadblock, 0 means you can pass through 

    e.g.
    [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    the result = [
        [0,0],[0,1],[0,2],[0,3],[0,4],
        [1,4],
        [2,4],
        [3,4],
        [4,4]
    ]

    note: another path here [
        [0,0],[0,1],[0,2],[0,3],[0,4],
        [1,4],
        [2,4],[2,3],[2,2]
        [3,4],
        [4,4]
    ] is not a shortest path
"""

"""
    1st approach: BFS + hastable
    - To find the path, just keep track of the previous cell(source) at every cell. 
    - Dont worry if a cell might have multiple sources. 
    The reason is since we use a hashtable, every cell will be just visited once and it is guaranteed that the first-visit must be from the shortest sub-path
"""


def f(matrix):
    R, C = len(matrix), len(matrix[0])
    q = []
    q.append([0, 0, None])  # i, j, previous cell
    seen = set()
    source_of_every_cell = defaultdict(tuple)
    path_found = False
    while len(q) > 0:
        i, j, prev = q.pop(0)
        if i < 0 or i == R or j < 0 or j == C:
            continue
        if matrix[i][j] != 0:
            continue
        key = (i, j)
        if key in seen:
            continue
        seen.add(key)
        source_of_every_cell[key] = prev
        if i == R-1 and j == C-1:
            path_found = True
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            q.append((i+di, j+dj, key))
    if path_found:
        path = []
        cur = (R-1, C-1)
        while cur != (0, 0):
            path.append(cur)
            cur = source_of_every_cell[cur]
        return [(0, 0)] + path[::-1]
    return []


a = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
]
print(f(a))
