def f():
    n = int(input())
    for _ in range(n):
        x = int(input())
        d = x // 2020
        r = x % 2020
        if r > d or d == 0:
            print("NO")
        else:
            print("YES")


f()
