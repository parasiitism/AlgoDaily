"""
    Time    O(N)    108 ms
    Space   O(1)    19700 KB
"""


def f():
    n = int(input())
    x = 0
    for i in range(n):
        s = input()
        if '++' in s:
            x += 1
        if '--' in s:
            x -= 1
    return x


print(f())
