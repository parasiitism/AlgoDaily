def f():
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        B = [int(x) for x in input().split()]
        print(solve(A, B))


def solve(A, B):
    n = len(A)
    min1 = min(A)
    min2 = min(B)
    res = 0
    for i in range(n):
        ops = max(A[i] - min1, B[i] - min2)
        res += ops
    return res


f()
