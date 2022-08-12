
def f():
    n = int(input())
    res = 0
    for _ in range(n):
        p, q = [int(x) for x in input().split()]
        cap = q - p
        if cap >= 2:
            res += 1
    print(res)


f()
