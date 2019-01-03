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


class Solution1(object):
    """
    iterative dfs
    Time    O(2^n)
    Space   O(2^n)
    beats   3.67%
    """

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        stack = [(nums, [])]  # array of tuples (nums, path)
        while len(stack) > 0:
            pop = stack.pop()
            arr = pop[0]
            path = pop[1]
            result.append(path)
            for i in range(len(arr)):
                stack.append((arr[i+1:], path+[arr[i]]))
        return result


print(Solution().subsets([1, 2, 3]))
