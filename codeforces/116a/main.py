
"""
    1st approach: binary search

    Time    O(7)
    Space   O(1)
"""


def f():
    n = int(input())
    res = 0
    cur = 0
    for _ in range(n):
        a, b = [int(s) for s in input().split(" ")]
        cur -= a
        cur += b
        res = max(res, cur)
    return res


print(f())
