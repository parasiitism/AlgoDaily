def f():
    n = int(input())
    for _ in range(n):
        L = int(input())
        half = L//2 + 1
        res = []
        for i in range(L//2):
            res.append(half+i)
            res.append(i+1)
        if L % 2 == 1:
            res.append(L)
        print(" ".join([str(x) for x in res]))


f()
