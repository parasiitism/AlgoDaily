"""
    1st: sort

    Time    O(NlogN)
    Space   O(N)
    120 ms, faster than 7.16%
"""


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        arr = sorted(nums)
        res = 0
        for i in range(1, len(arr)):
            res = max(res, arr[i]-arr[i-1])
        return res


"""
    2nd: sort

    Time    O(NlogN)
    Space   O(1)
    80 ms, faster than 20.57%
"""


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            res = max(res, nums[i]-nums[i-1])
        return res


"""
    Further:

    The suggested solutions are radix-sort OR bucket-sort, 
    which i dont think interviewers would ask you to implement it in an interview
"""
