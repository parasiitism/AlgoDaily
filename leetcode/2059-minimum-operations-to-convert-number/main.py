from collections import *

"""
    1st: BFS

    Time    O(N^N -> N) every number branches out N nodes, but every number will be seen once only, so hard to determine
    Space   O(N) the hashset
    5248 ms, faster than 100.00%
"""


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = deque()
        q.append((start, 0))
        seen = set()
        while len(q) > 0:
            n, steps = q.popleft()
            if n == goal:
                return steps
            if n < 0 or n > 1000:
                continue
            if n in seen:
                continue
            seen.add(n)
            for cand in nums:
                x = n + cand
                y = n - cand
                z = n ^ cand
                q.append((x, steps + 1))
                q.append((y, steps + 1))
                q.append((z, steps + 1))
        return -1
