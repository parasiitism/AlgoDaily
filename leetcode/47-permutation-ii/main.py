# optimize the naive approach
# recursively dfs all the possibilities and avoid duplicate paths by using a hashtable

# e.g. 2, -1, 3, -1
# sort it such that nums = -1, -1, 2, 3

# compute permutations of - 1(index 0)
# skip computation for index 1 becos - 1(index 0) has been considered
# compute permutations of 2(index 2)
# compute permutations of 3(index 3)

# time    O(n!) worst case
# space	O(n!)
# beats 46.47%


class Solution(object):

    def __init__(self):
        self.result = []

    def permuteUnique(self, nums):
        nums = sorted(nums)
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, prefix):
        if len(nums) == 0:
            self.result.append(prefix)
        visited = {}
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited[nums[i]] = True
            self.dfs(nums[:i] + nums[i+1:], prefix + [nums[i]])


s = Solution()
print(s.permuteUnique([1, 1, 2]))
