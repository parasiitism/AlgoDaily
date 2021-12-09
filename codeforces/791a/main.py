"""
    1st approach: binary search

    Time    O(7)
    Space   O(1)
"""


def f():
    a, b = [int(s) for s in input().split(" ")]
    left, right = 0, 100
    while left < right:
        mid = (left + right)//2
        if a*(3**mid) <= b*(2**mid):
            left = mid + 1
        else:
            right = mid
    return left


print(f())
