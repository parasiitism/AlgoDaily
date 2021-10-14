"""
    1st: sort
    - similar to leetcode462
    - find the median
    - sum the diff between the median and every number

    Why median works:
    (v[j] - v[i]) % x == 0 for all 0 <= i < j < len(nums)

    Time    O(NlogN)
    Space   O(N)
    1668 ms, faster than 9.09%
"""


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                nums.append(grid[i][j])
        nums.sort()
        n = len(nums)
        median = nums[n//2]
        res = 0
        for num in nums:
            if abs(num - median) % x != 0:
                return -1
            res += abs(num - median) // x
        return res
