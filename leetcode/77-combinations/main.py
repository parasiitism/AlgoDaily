class Solution(object):
    """
    Implementation similar to permutations
    Time O(nCk)
    Space O(nCk) due to the recrusion
    beats 13.88%
    """

    def __init__(self):
        self.result = []

    def combine(self, n, k):
        if k < 1 or k > n:
            return []
        nums = []
        for i in range(n):
            nums.append(i+1)
        self.dfs(nums, [], k)
        return self.result

    def dfs(self, nums, path, k):
        if len(path) == k:
            self.result.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[i+1:], path + [nums[i]], k)


r = Solution().combine(4, 2)
print(r)
r = Solution().combine(4, 3)
print(r)
r = Solution().combine(5, 4)
print(r)


class Solution1(object):
    """
    Implementation similar to permutations
    Time O(nCk)
    Space O(nCk) due to the recrusion
    beats 21.53%
    """

    def __init__(self):
        self.result = []

    def combine(self, n, k):
        if k < 1 or k > n:
            return []
        self.dfs(1, n, [], k)
        return self.result

    def dfs(self, start, n, path, k):
        if len(path) == k:
            self.result.append(path)
        else:
            for i in range(start, n+1):
                self.dfs(i+1, n, path + [i], k)


r = Solution1().combine(4, 2)
print(r)
r = Solution1().combine(4, 3)
print(r)
r = Solution1().combine(5, 4)
print(r)
