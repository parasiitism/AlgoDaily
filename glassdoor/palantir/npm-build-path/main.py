from collections import *


def findOrder(n, deps):
    G = {}
    indegrees = {}
    for i in range(n):
        G[i] = []
        indegrees[i] = 0

    for package, dep in deps:
        G[dep].append(package)
        indegrees[package] += 1

    q = deque()
    for package in indegrees:
        if indegrees[package] == 0:
            q.append(package)

    res = []
    while len(q) > 0:
        package = q.popleft()
        res.append(package)
        children = G[package]
        for child in children:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                q.append(child)
    if len(res) != n:
        return []
    return res


print(findOrder(6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2]]))
# [5, 2, 4, 1, 3, 0]

print(findOrder(6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2], [5, 3]]))
# []

print(findOrder(1, []))
# [0]
