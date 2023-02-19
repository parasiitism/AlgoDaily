"""
    1st: dynamic programming (bottom-up)
    - at every point, we calculate the max filth from the previous filth dp[i-1] or dp[i-2] + nums[i]

    Time    O(N)
    Space   O(N)
    20 ms, faster than 98.72%
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = n * [0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]

"""
    2nd: dynamic programming (top-down)
    - at every point, 2 cases
        - if we rob, go to the 2nd next house
        - else, go to the next house
        we just need the max amongst them, cache them for avoiding re-calculation

    Time    O(N)
    Space   O(N)
    20 ms, faster than 52.67%
"""
class Solution(object):
    def rob(self, nums):
        cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            a = dfs(i+1)
            b = dfs(i+2) + nums[i]
            best = max(a, b)
            cache[i] = best
            return cache[i]
        return dfs(0)

"""
    3rd approach: dynamic programming with only vars
    
    Time    O(N)
    Space   O(1)
    12 ms, faster than 98.42% 
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob = 0
        notRob = 0
        for x in nums:
            temp = rob
            rob = max(rob, notRob + x)
            notRob = temp
        return max(rob, notRob)


"""
    followup: what if there are negative numbers? lets say the thieves might lose money by visiting a house
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        included = nums[0]
        excluded = 0
        for i in range(1, len(nums)):
            temp = included
            # the crux is: the filth must be >= 0
            included = max(excluded + max(nums[i], 0), included)
            excluded = temp
        return included
