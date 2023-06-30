"""
    recursion
    - simple but annoying to implement

    Time    O(N * 2^7) 7 means 1000^2
    Space   O(2^7)
"""


class Solution:

    def canSplit(self, xx, x):

        def split(remain, subs):
            if len(remain) == 0:
                total = 0
                for sub in subs:
                    total += int(sub)
                if total == x:
                    return True
                return False

            for i in range(len(remain)):
                b = split(remain[i+1:], subs + [remain[:i+1]])
                if b:
                    return b

        return split(str(xx), [])

    def punishmentNumber(self, n: int) -> int:
        res = 0
        for x in range(1, n+1):
            if self.canSplit(x*x, x):
                res += x*x
        return res
