"""
    math
    - The answer depends on minimum(m, n)
    - If min(n, m) is odd, then Akshat will win. Otherwise Malvika will win.
"""


def f():
    n, m = map(int, input().split())
    if n > m:
        m, n = n, m
    if n % 2 == 0:
        return "Malvika"
    return "Akshat"


print(f())
