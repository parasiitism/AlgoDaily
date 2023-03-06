"""
    1st approach: recursion + hashtable

    Recursive DFS using hashtables to avoid duplicates, see ./idea.jpeg
    Method similar to what I did for Permutation II

    Time    O(2^N) worst
    Space   O(2^N) recursion
    24 ms, faster than 100.00%
"""


class Solution(object):

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


"""
    2nd approach: recursion
    - similar to 1st dont need to use a hashtable(since the array is sorted)
    
    Time    O(2^N) worst
    Space   O(2^N) recursion
    24 ms, faster than 100.00%
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, chosen):
        self.res.append(chosen)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:], chosen + [nums[i]])
            """
            OR
            
            if i == 0 or nums[i-1] != nums[i]:
                self.dfs(nums[i+1:], chosen + [nums[i]])
            """

s = Solution()

print(s.subsetsWithDup([1, 2, 2, 3]))