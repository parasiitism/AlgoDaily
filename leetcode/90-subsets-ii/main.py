class Solution(object):
    """
    Recursive DFS using hashtables to avoid duplicates, see ./idea.jpeg
    Method similar to what I did for Permutation II
    Time    O(2^n) worst
    Space   O(2^n) recursion
    beats   41.22%
    """

    def __init__(self):
        self.result = []

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, path):
        self.result.append(path)
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            seen[nums[i]] = True
            self.dfs(nums[i+1:], path+[nums[i]])


print(Solution().subsetsWithDup([1, 2, 2, 1, 3]))
