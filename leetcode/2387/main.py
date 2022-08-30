"""
    binary search

    Time    O(log(10**6) * RlogC)
    Space   O(1)
    1328 ms, faster than 100.00%
"""


class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        left = 0
        right = 10**6
        target = (R*C)//2
        while left < right:
            mid = (left + right) // 2
            count = 0
            for i in range(R):
                count += bisect.bisect_right(grid[i], mid)
            if target >= count:
                left = mid + 1
            else:
                right = mid
        return left
