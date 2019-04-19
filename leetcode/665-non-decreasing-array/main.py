"""
    1st approach:
    - copy the arr and move forward, and if we meet a smaller number, we set our previous number down to this number
    - copy the arr and move backward, and if we meet a bigger number, we set our previous number up to this number
    - check if either forward and backward is non-decreasing

    Time    O(4n)
    Space   O(n)
    204 ms, faster than 22.42%
"""


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return True
        a = nums[:]
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                a[i-1] = a[i]
                break

        b = nums[:]
        for i in range(len(b)-2, -1, -1):
            if b[i] > b[i+1]:
                b[i+1] = b[i]
                break

        checkA = True
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                checkA = False

        checkB = True
        for i in range(1, len(b)):
            if b[i] < b[i-1]:
                checkB = False

        return checkA or checkB
