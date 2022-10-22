"""
    1st: brute-force

    Time    O(QN)
    Space   O(N)
    LTE
"""


class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        nodes = n * [0]
        for x in queries:
            x -= 1
            q = [x]
            while len(q) > 0:
                idx = q.pop(0)
                nodes[idx] = 1 - nodes[idx]
                if idx * 2 + 1 < n:
                    q.append(idx * 2 + 1)
                if idx * 2 + 2 < n:
                    q.append(idx * 2 + 2)
        return sum(nodes)


"""
    2nd: BFS
    - record the number of times to flip for each of the node
    - do BFS once at the end to count the flips (remember to consider the flips from parent too)

    Time    O(Q+N)
    Space   O(N)
    6043 ms, faster than 100.00%
"""


class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        counts = n * [0]
        for x in queries:
            x -= 1  # transform to 0-indexed
            counts[x] += 1
        q = [(0, 0)]  # (node idx, number of flips)
        while len(q) > 0:
            idx, parent_count = q.pop(0)
            val = (counts[idx] + parent_count) % 2
            counts[idx] = val
            if idx * 2 + 1 < n:
                q.append((idx * 2 + 1, val))
            if idx * 2 + 2 < n:
                q.append((idx * 2 + 2, val))
        return sum(counts)


"""
    3rd: DSF
    - same as 2nd but using DFS

    Time    O(Q+N)
    Space   O(N+N)
    3090 ms, faster than 100.00%
"""


class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        counts = n * [0]
        for x in queries:
            x -= 1  # transform to 0-indexed
            counts[x] += 1

        def dfs(idx, parent_count):
            if idx >= n:
                return
            val = (counts[idx] + parent_count) % 2
            counts[idx] = val
            if idx * 2 + 1 < n:
                dfs(idx * 2 + 1, val)
            if idx * 2 + 2 < n:
                dfs(idx * 2 + 2, val)
        dfs(0, 0)
        return sum(counts)
