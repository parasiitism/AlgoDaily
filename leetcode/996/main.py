import math

"""
    Recursion

    Time    Worst O(N!), however it is rare that 
    Space   O(N)
"""


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        nums.sort()
        self.res = []
        for i in range(len(nums)):

            # skip the duplicate number if redundant
            if i > 0 and nums[i] == nums[i-1]:
                continue

            x = nums[i]
            self.dfs([x], nums[:i] + nums[i+1:])
        # print(self.res)
        return len(self.res)

    def dfs(self, chosen, nums):
        # print(chosen, nums)
        if len(nums) == 0:
            self.res.append(chosen)
            return
        for i in range(len(nums)):

            # skip the duplicate number if redundant
            if i > 0 and nums[i] == nums[i-1]:
                continue

            x = nums[i]
            y = chosen[-1] + x
            if math.floor(math.sqrt(y))**2 == y:
                self.dfs(chosen + [x], nums[:i] + nums[i+1:])
