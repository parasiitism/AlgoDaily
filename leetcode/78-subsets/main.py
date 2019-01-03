class Solution(object):
    """
    Recursive DFS
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
    Iterative DFS
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


print(Solution1().subsets([1, 2, 3]))


class Solution2(object):
    """
    Iteratively append the next item to calculated items
    e.g. [1,2,3]
    []
    [],[1]
    [],[1],[2],[1,2]
    [],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]
    Time    O(2^n)
    Space   O(2^n)
    beats   35.29%
    """

    def subsets(self, nums):
        res = [[]]
        for num in nums:
            n = len(res)
            for i in range(n):
                res += [res[i]+[num]]
            # the above 3 lines can be reduced as res += [item+[num] for item in res] # but only beats 15.25%
        return res


print(Solution2().subsets([1, 2, 3]))
