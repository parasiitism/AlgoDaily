"""
    BFS
    Time    O(10000)
    Space   O(10000)
"""


def f():
    m, n = [int(x) for x in input().split()]
    seen = set()
    q = [(m, 0)]
    while len(q) > 0:
        x, steps = q.pop(0)
        if x == n:
            return steps
        if x < 0:
            continue
        if abs(x - n) >= 10**4:
            continue
        if x in seen:
            continue
        seen.add(x)
        q.append((x * 2, steps + 1))
        q.append((x - 1, steps + 1))
    return -1


print(f())
