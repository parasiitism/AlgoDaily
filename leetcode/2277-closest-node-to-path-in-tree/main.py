from collections import *

"""
    DFS + BFS + hashtable
    1. build a graph
    2. for each query
        - do DFS to find a path between 2 nodes, and put the nodes in a hashset
            - since this is a tree, we can just use a hashset to avoide redundant visit
        - do BFS from target node to see which node in hashset is the nearest

    Time    O(N + QN)
    Space   O(N)
    7072 ms, faster than 100.00%
"""


class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # build a graph
        G = defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        # for each query
        res = []
        for u, v, target in query:
            # DFS
            nodes_in_the_path = set()
            stack = [(u, [u])]
            seen = set()
            while len(stack) > 0:
                node, path = stack.pop()
                if node in seen:
                    continue
                seen.add(node)
                if node == v:
                    nodes_in_the_path = set(path)
                    break
                for nb in G[node]:
                    stack.append((nb, path + [nb]))
            # BFS
            seen = set()
            q = [(target, 0)]
            while len(q) > 0:
                node, steps = q.pop(0)
                if node in nodes_in_the_path:
                    res.append(node)
                    break
                if node in seen:
                    continue
                seen.add(node)
                for nb in G[node]:
                    q.append((nb, steps))
        return res
