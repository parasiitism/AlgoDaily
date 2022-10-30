def f():
    n = int(input())
    for _ in range(n):
        l = input()
        s = input()
        q = 0
        for c in s:
            if c == 'Q':
                q += 1
            else:
                q = max(q - 1, 0)
        if q == 0:
            print("Yes")
        else:
            print("NO")


f()
