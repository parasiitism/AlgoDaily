"""
    1st: BFS

    Time    O(N) <- it is hard to determine in K, digit1, digit2
    Space   O(N)
    114 ms, faster than 100.00%
"""


class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        a = min(digit1, digit2)
        b = max(digit1, digit2)
        q = [0]
        visited = set()
        while len(q) > 0:
            node = q.pop(0)
            if node in visited:
                continue
            if node > 2 ** 31 - 1:
                continue
            if node > k and node % k == 0:
                return node
            visited.add(node)
            q.append(node * 10 + a)
            q.append(node * 10 + b)
        return -1
