"""
    recursive dfs + memorization
    - dfs to traverse the path from bottom
    - if we see a (idx, total) that we previously visited, we can just use the previous result because the way come up with the remain would be the same

    Time    O(n^2)
    Space   O(n)
    440 ms, faster than 23.93%
"""


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        seen = {}
        return self.dfs(nums, 0, 0, S, seen)

    def dfs(self, nums, idx, total, S, seen):
        if idx == len(nums):
            if total == S:
                return 1
            return 0
        if (idx, total) in seen:
            return seen[(idx, total)]
        x = nums[idx]
        a = self.dfs(nums, idx+1, total + x, S, seen)
        b = self.dfs(nums, idx+1, total - x, S, seen)
        seen[(idx, total)] = a + b
        return a + b
