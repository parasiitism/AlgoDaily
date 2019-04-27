"""
    1st approach: dynamic programming

    very similar to lc300

    the basic idea is, instead of storing a list of counts [1,1,1,1,1]
    we store a list of [count, possibilites]
    [
        [1:1],
        [1:1],
        [1:1],
        [1:1],
        [1:1],
    ]

    e.g.
    1,   3,   5,   4,   7,   7,   7,   8
    [1,1]<1,1><1,1><1,1><1,1><1,1><1,1><1,1>
         [2,1]<2,1><2,1><2,1><2,1><2,1><2,1>
              [3,1][3,1]<3,1><3,1><3,1><3,1>
                        <4,1><4,1><4,1><4,1>
                        [4,2][4,2][4,2]<4,2>
                                       <5,2>
                                       <5,4>
                                       [5,6]
    Time    O(n^2)
    Space   O(n)
    804 ms, faster than 25.62%
"""


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for _ in range(len(nums)):
            dp.append([1, 1])
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    curLen = dp[j][0] + 1
                    if curLen > dp[i][0]:
                        # if >, we update the posibilites to that of dp[j]
                        dp[i] = [curLen, dp[j][1]]
                    elif curLen == dp[i][0]:
                        # if ==, we increment the posibilites to that of dp[j]
                        dp[i][1] += dp[j][1]
        resLen = 0
        resCount = 0
        for l, c in dp:
            if l > resLen:
                resLen = l
                resCount = c
            elif l == resLen:
                resCount += c
        return resCount
