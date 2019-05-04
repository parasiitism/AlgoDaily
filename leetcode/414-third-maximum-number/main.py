"""
    1st approach:
    - 3 variables and update them coorespondingly

    Time    O(n)
    Space   O(n)
    40 ms, faster than 50.40%
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = -sys.maxsize
        second = -sys.maxsize
        third = -sys.maxsize
        for num in nums:
            if num > largest:
                third = second
                second = largest
                largest = num
            elif num < largest and num > second:
                third = second
                second = num
            elif num < second and num > third:
                third = num
        if third == -sys.maxsize:
            return largest
        return third
