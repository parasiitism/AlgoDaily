"""
    encrpyt the matrix in 2 steps:
    
    abc             ro          djp
    def            qnli         agm
    ghi     ->    pmkhfc    ->  ekq
    jkl            jgeb         bhn
    mno             ba          flr
    pqr                         cio
"""


def f(M):
    R, C = len(M), len(M[0])  # R = 2*C
    res = []
    for j in range(C):
        row1 = []
        i = 1
        while i < R:
            row1.append(M[i][j])
            i += 2
        res.append(row1)

        row2 = []
        i = 0
        while i < R:
            row2.append(M[i][j])
            i += 2
        res.append(row2)
    return res


M = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r'],
]
print(f(M))
