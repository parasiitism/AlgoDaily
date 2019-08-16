"""
    1st approach: recursion + hashtable
    - similar to classic coin change/knapsack problem
    - when we calculate recursively, there must be some redundant 'subtrees'. we can use a hashtable to avoid redundant calculation

    Time    O(DFT)
    Space   O(DF)
    748 ms, faster than 39.83%
"""


class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        ht = {}
        total = self.dfs(target, d, f, ht)
        return total % (10**9+7)

    def dfs(self, remain, d, f, ht):
        if d == 0:
            if remain == 0:
                return 1
            else:
                return 0
        if (remain, d) in ht:
            return ht[(remain, d)]
        total = 0
        for i in range(1, f+1):
            total += self.dfs(remain-i, d-1, f, ht)
        ht[(remain, d)] = total
        return total
