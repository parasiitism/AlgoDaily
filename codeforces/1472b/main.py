from collections import *

"""
    math/logic

    For cases = true,
    - sum must be EVEN
    - Either
        - # of 1 >= 2, e.g. 2, 2, 1 is never gonna have EVEN sum
        - # of 1 == 0 BUT # of 2 is EVEN

    Time    O(N)
    Space   O(N)
"""


def f():
    t = int(input())
    for _ in range(t):
        _ = int(input())
        candies = [int(x) for x in input().split()]
        print(check(candies))


def check(candies):
    total = sum(candies)
    if total % 2 == 1:
        return "NO"
    ctr = Counter(candies)
    if ctr[1] >= 2:
        return "YES"
    if ctr[1] == 0 and ctr[2] % 2 == 0:
        return "YES"
    return "NO"


f()
