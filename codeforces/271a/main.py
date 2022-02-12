
"""
    Time    O(N)
    Space   O(N)
"""


def f():
    x = int(input()) + 1
    while x < 10000:
        keys = set([c for c in str(x)])
        if len(keys) == 4:
            return x
        x += 1
    return -1


print(f())
