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
        if len(nums) == 0:
            return 0
        seen = {}
        return self.dfs(nums, 0, 0, S, seen)

    def dfs(self, nums, idx, total, S, seen):
        if idx == len(nums) and total == S:
            return 1
        if idx < len(nums):
            if (idx, total) in seen:
                return seen[(idx, total)]
            a = self.dfs(nums, idx+1, total+nums[idx], S, seen)
            b = self.dfs(nums, idx+1, total-nums[idx], S, seen)
            seen[(idx, total)] = a + b
            return a + b
        return 0
