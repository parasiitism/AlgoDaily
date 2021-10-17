
"""
    Time    O(N)    154 ms
    Space   O(1)    6568 KB
"""


def f():
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end
    n, k, t = map(int, input().split())
    total = n * k * t // 100
    fullSquartCount, remain = total // k, total % k
    res = n * [0]
    for i in range(fullSquartCount):
        res[i] = k
    if remain > 0:
        res[fullSquartCount] = remain
    for x in res:
        print(x, end=" ")


f()
