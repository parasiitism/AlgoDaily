class Solution(object):
    """
    recursive dfs
    Time    O(2^n)
    Space   O(2^n) recursion
    beats   35.29%
    """

    def __init__(self):
        self.result = []

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, path):
        self.result.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]])


print(len(Solution().subsets([1, 2, 3, 4, 5])))
