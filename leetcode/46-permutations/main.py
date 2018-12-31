class Solution(object):

    def __init__(self):
        self.result = []

    def permute(self, nums):
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, prefix):
        if len(nums) == 0:
            self.result.append(prefix)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], prefix + [nums[i]])


s = Solution()
print(s.permute([1, 2, 3]))
