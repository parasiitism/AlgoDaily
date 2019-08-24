from collections import *

"""
    1st approach: combination sum

    Time    at worst O(2^n)
    Space   O(n)
    LTE
"""


class Solution(object):

    def __init__(self):
        self.combos = []

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidates = []
        for i in range(1, n):
            candidates.append(i)
        self.dfs(candidates, n, [], 0)
        res = 0
        for combo in self.combos:
            product = 1
            for x in combo:
                product *= x
            res = max(res, product)
        return res

    def dfs(self, candidates, target, path, total):
        if total == target:
            self.combos.append(path)
        elif total < target:
            for i in range(len(candidates)):
                can = candidates[i]
                if len(path) == 0 or path[-1] <= can:
                    self.dfs(candidates, target, path+[can], total+can)


s = Solution()
print(s.integerBreak(2))
print(s.integerBreak(7))
print(s.integerBreak(8))
print(s.integerBreak(9))
print(s.integerBreak(10))
print(s.integerBreak(20))

"""
    2nd: bottom DP, learned from others
    - the point is we have to come up with max(x, dp[x]) * max(target-x, dp[target-x])

    e.g. 9
    1+8, 2+7, 3+6, 4+5

    e.g. 10
    1+9, 2+8, 3+7, 4+6, 5+5

    ref:
    - https://leetcode.com/problems/integer-break/discuss/80717/DP-Python-Solution
    
    Time    O(n^2)
    Space   O(n)
    12 ms, faster than 93.72%
"""


class Solution(object):

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = (n+1) * [0]
        for num in range(2, n+1):
            for x in range(1, num/2+1):
                y = num - x
                res = max(x, dp[x]) * max(y, dp[y])
                dp[num] = max(dp[num], res)
        return dp[n]


"""
    the 3rd way is a math approach in O(N), I dont understand it so wont keep it here

    ref:
    - https://leetcode.com/problems/integer-break/discuss/80721/Why-factor-2-or-3-The-math-behind-this-problem.
    - https://leetcode.com/problems/integer-break/discuss/80689/A-simple-explanation-of-the-math-part-and-a-O(n)-solution
"""
