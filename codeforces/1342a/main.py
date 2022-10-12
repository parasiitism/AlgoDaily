"""
    tuto: https://codeforces.com/blog/entry/76633

    Time    O(N)
"""


def f():
    for _ in range(int(input())):
        x, y = map(int, input().split())
        a, b = map(int, input().split())
        # 2 operatoin A = b, we just need the minimal one
        b = min(b, a + a)
        # easier for calculation: x >= y must be
        if x < y:
            x, y = y, x
        print(y * b + (x - y) * a)


f()
