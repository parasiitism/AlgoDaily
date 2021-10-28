"""
    Time    O(N)    108 ms
    Space   O(1)    19700 KB
"""


def f():
    n = int(input())
    res = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        if a+b+c >= 2:
            res += 1
    return res


print(f())
