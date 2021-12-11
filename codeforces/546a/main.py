
"""
    1st approach: math

    Time    O(1)
    Space   O(1)
"""


def f():
    k, n, w = [int(s) for s in input().split(" ")]
    target = ((1+w) * w // 2) * k
    return max(target - n, 0)


print(f())
