
from collections import *

"""
    BFS

    Time    O(N)
    Space   O(N)
"""


def f():
    n, m = [int(x) for x in input().split()]
    cat_at_nodes = [0] + [int(x) for x in input().split()]
    graph = defaultdict(set)

    for _ in range(n-1):
        u, v = [int(x) for x in input().split()]
        graph[u].add(v)
        graph[v].add(u)

    res = set()
    seen = set()

    q = [(1, 0)]
    while len(q) > 0:
        node, cat_count = q.pop(0)

        # deduplicate
        if node in seen:
            continue
        seen.add(node)

        # check m consecutive
        if cat_at_nodes[node] == 0:
            cat_count = 0
        else:
            cat_count += cat_at_nodes[node]
        if cat_count > m:
            continue

        # check leaf
        if len(graph[node]) == 0:
            res.add(node)

        for nb in graph[node]:
            graph[nb].remove(node)  # remove the counterpart
            q.append((nb, cat_count))

    if 1 in res:
        res.remove(1)
    return len(res)


print(f())
