"""
    1st: sliding window
    1. count the number of ones
    2. make it easy to deal with the circular case
    3. the result is the minimum number of "holes" in our sliding window while we iterate the array

    Time    O(N)
    Space   O(2N)
    1699 ms, faster than 75.00%
"""


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # 1
        totalOnes = sum(nums)
        # 2
        A = nums + nums
        # 3
        zeros = 0
        res = 2**32
        j = 0
        for i in range(len(A)):
            if A[i] == 0:
                zeros += 1
            if i >= totalOnes:
                if A[j] == 0:
                    zeros -= 1
                j += 1
            if i >= totalOnes-1:
                res = min(res, zeros)
        return res
