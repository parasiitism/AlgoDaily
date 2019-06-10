"""
    1st approach: dynamic programming

    ref: Longest Increasing Subsequence
    - https://www.youtube.com/watch?v=CE2b_-XfVDk

    Time    O(n^2)
    Space   O(n)
    LTE
"""


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = len(nums) * [1]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        res = 0
        for x in dp:
            res = max(res, x)
        return res >= 3


"""
    2nd approach: back and forth array
    - similar to lc42, 842, 915
    - from the front to the end, store the min at each index
    - from the end to the front, store the max at each index
    - when forward[i] < num[i] < backward[i], there is a result

    e.g.        [8,3,5,1,6]
    forward ->   8 3 3 1 1
    backward <-  8 6 6 6 6  
    at index 2, forward[2] < nums[2] < backward[2] = 3 < 5 < 6

    Time    O(n)
    Space   O(n)
    48ms beats 37.05%
"""


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        dip = sys.maxsize
        forward = []
        for num in nums:
            dip = min(dip, num)
            forward.append(dip)

        peak = -sys.maxsize
        backward = []
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            peak = max(peak, num)
            backward.append(peak)
        backward = backward[::-1]

        for i in range(len(nums)):
            if forward[i] < nums[i] < backward[i]:
                return True
        return False
