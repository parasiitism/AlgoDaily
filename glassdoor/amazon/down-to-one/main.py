"""
    https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=484422&extra=&page=4
"""


class Solution(object):
    def __init__(self):
        self.result = []

    def toOne(self, n):
        self.helper(n, [])
        return self.result

    def helper(self, n, path):
        if n == 0:
            return
        if n == 1:
            self.result.append(path+[n])
        elif n % 2 == 0:
            self.helper(n/2, path+[n])
        else:
            self.helper(n+1, path+[n])
            self.helper(n-1, path+[n])


print(Solution().toOne(5))
