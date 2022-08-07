"""
    Time    O(digits)
    Space   O(digits)
"""


def f():
    s = input()
    res = 0
    for c in s:
        d = int(c)
        if res == 0 and d == 9:
            res = res * 10 + d
        else:
            mi = min(d, 9 - d)
            res = res * 10 + mi
    print(res)


f()
