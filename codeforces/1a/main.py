from math import *


def f():
    n, m, a = map(int, input().split())
    r = ceil(n/a)
    c = ceil(m/a)
    return r * c


print(f())
