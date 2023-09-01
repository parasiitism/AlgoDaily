"""
    Task 1: Find all the peaks on a map. It is guraunteed that there is no adjacent cells share the same height

    input = [
        [1, 2, 3],
        [4, 5, 8],
        [9, 7, 0]
    ]
    output = [
        [0, 0, 0],
        [0, 0, 1],
        [1, 0, 0]
    ]

    Task 2: Assuming the peaks will flow something to the water(cell=0), indicate the cells where the water will flow through
    
    progess for peak at (1, 2) = [
        [1, 1, 1],
        [1, 1, 1],
        [0, 1, 1]
    ]

    progess for peak at (2, 0) = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 1, 1]
    ]

    output is the sum of them = [
        [2, 2, 2],
        [2, 2, 1],
        [1, 2, 2]
    ]
"""


def task1(M):
    R, C = len(M), len(M[0])
    res = []
    for _ in range(R):
        res.append(C * [0])

    # 8 directions
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for i in range(R):
        for j in range(C):

            is_peak = True
            for di, dj in dirs:
                ii, jj = i+di, j+dj
                if ii < 0 or ii >= R or jj < 0 or jj >= C:
                    continue
                if M[ii][jj] > M[i][j]:
                    is_peak = False
                    break
            if is_peak:
                res[i][j] = 1
    return res


a = [
    [1, 2, 3],
    [4, 5, 8],
    [9, 7, 0]
]
task1_result = task1(a)
print(task1_result)


def task2(M, task1_result):
    R, C = len(M), len(M[0])
    res = []
    for _ in range(R):
        res.append(C * [0])

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def bfs(x, y):
        q = [(x, y)]
        seen = set()
        while len(q) > 0:
            i, j = q.pop(0)
            if (i, j) in seen:
                continue
            seen.add((i, j))
            res[i][j] += 1
            for di, dj in dirs:
                ii, jj = i+di, j+dj
                if ii < 0 or ii >= R or jj < 0 or jj >= C:
                    continue
                if M[ii][jj] < M[i][j]:
                    q.append([ii, jj])

    for i in range(R):
        for j in range(C):
            if task1_result[i][j] == 1:
                bfs(i, j)

    return res


print(task2(a, task1_result))
