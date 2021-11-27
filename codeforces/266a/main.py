"""
    Time    O(N)    108 ms
    Space   O(1)    19700 KB
"""


def f():
    n = int(input())
    s = input()
    cur = ''
    res = 0
    for c in s:
        if c != cur:
            res += 1
            cur = c
    return n - res


print(f())
