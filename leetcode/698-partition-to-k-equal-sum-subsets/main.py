"""
    1st approach: backtracking
    - the naive approach is to explore all the subsets, O(2^n), but for each item we can use once only
    , so we need to cache the used item(by store the indices)
    - so we need to do backtracking(similar to lc51, 52)
        - try to include the next number
        - and 'backtrack' the next number if it fails
    - if we reach to the point where our curSum == target, we set k=k-1 and explore again from the begining of the input array 

    ref:
    - https://www.youtube.com/watch?v=qpgqhp_9d1s
    - https://segmentfault.com/a/1190000017013991
    - https://github.com/cherryljr/LeetCode/blob/master/Partition%20to%20K%20Equal%20Sum%20Subsets.java

    Time    from O(2^n) to O(n!) i actually dont know to determind
    Space   O(n) depth of recursion tree
    432ms beats 34%
"""


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        432ms beats 34%
        """
        total = sum(nums)
        if k == 0 or total % k != 0:
            return False
        target = total//k

        used = len(nums) * [False]
        return self.dfs(nums, target, 0, k, 0, used)

    def dfs(self, nums, target, curSum, k, start, used):
        if k == 1:
            return True
        if curSum == target:
            return self.dfs(nums, target, 0, k-1, 0, used)
        for i in range(start, len(nums)):
            if used[i] == False:
                used[i] = True
                if self.dfs(nums, target, curSum+nums[i], k, i+1, used):
                    return True
                used[i] = False
        return False


s = Solution()

# true
a = [4, 3, 2, 3, 5, 2, 1]
b = 4
print(s.canPartitionKSubsets(a, 4))

# false
a = [2, 2, 2, 2, 3, 4, 5]
b = 4
print(s.canPartitionKSubsets(a, 4))

# true
a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
b = 5
print(s.canPartitionKSubsets(a, b))

# true, very good test case
a = [10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6]
b = 3
print(s.canPartitionKSubsets(a, b))
