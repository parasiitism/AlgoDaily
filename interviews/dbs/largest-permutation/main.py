class Solution(object):
    def __init__(self):
        self.res = 0

    def largestPermutation(self, nums):
        self.dfs(nums, 0)
        return self.res

    def dfs(self, nums, prefix):
        if len(nums) == 0:
            self.res = max(self.res, prefix)
        for i in range(len(nums)):
            x = nums[i]
            n = 0
            while x > 0:
                x /= 10
                n += 1
            self.dfs(nums[:i]+nums[i+1:], prefix*10**n+nums[i])


print(Solution().largestPermutation([54, 546, 548, 60]))
print(Solution().largestPermutation([1, 34, 3, 98, 9, 76, 45, 4]))
