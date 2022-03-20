"""
    1st: array
    - a lot of corner cases

    Time    O(N)
    Space   O(1)
    974 ms, faster than 23.06% 
"""


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # if there is only one element and k is odd, impossible
        if n == 1 and k % 2 == 1:
            return -1
        # get the max out of the limit we have
        maxNum = -1
        for i in range(min(k-1, n)):
            maxNum = max(maxNum, nums[i])
        # if we remove all, the top most one remained might be the result
        if k < n:
            maxNum = max(maxNum, nums[k])
        return maxNum
