"""
    1st: 2 arrays
    - count zeros from the left
    - count ones from the right
    - find the points where the score are max

    Time    O(N)
    Space   O(N)
    7769 ms, faster than 8.33% 
"""


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftMostCut = sum(nums)
        rightMostCut = n - leftMostCut

        largest = max(leftMostCut, rightMostCut)

        left = n * [0]
        zeros = 0
        for i in range(n):
            if nums[i] == 0:
                zeros += 1
            left[i] = zeros

        right = n * [0]
        ones = 0
        for i in range(n-1, -1, -1):
            if nums[i] == 1:
                ones += 1
            right[i] = ones

        for i in range(n-1):
            largest = max(largest, left[i] + right[i+1])

        res = []
        if largest == leftMostCut:
            res.append(0)
        if largest == rightMostCut:
            res.append(n)
        for i in range(n-1):
            if largest == left[i] + right[i+1]:
                res.append(i+1)

        return res
