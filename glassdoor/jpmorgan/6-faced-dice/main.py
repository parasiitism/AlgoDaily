"""
    https://www.1point3acres.com/bbs/thread-162067-1-1.html
"""


class Solution():
    def __init__(self):
        self.m = {}

    def dfs(self, n):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if n in self.m:
            return self.m[n]
        total = 0
        for i in range(1, 7):
            total += self.dfs(n-i)
        self.m[n] = total
        return total


s = Solution()
print(s.dfs(6))
print(s.dfs(610))
