"""
    Given a map of heights, find the plateauss

    input = [
        [1, 2, 3, 4],
        [5, 5, 5, 2],
        [1, 1, 1, 1],
        [0, 0, 0, 9]
    ]
    output = [
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ]
    note: neighbors are from 8 directions instead of 4 directions
"""


def mountain_plateaus(M):
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
    [1, 2, 3, 4],
    [5, 5, 5, 2],
    [1, 1, 1, 1],
    [0, 0, 0, 9]


]
print(mountain_plateaus(a))
