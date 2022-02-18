
def f():
    N = int(input())
    mat = []
    for _ in range(N):
        row = [int(s) for s in input().split(" ")]
        mat.append(row)
    R, C = len(mat), len(mat[0])
    for j in range(C):
        total = 0
        for i in range(R):
            total += mat[i][j]
        if total != 0:
            return 'NO'
    return 'YES'


print(f())
