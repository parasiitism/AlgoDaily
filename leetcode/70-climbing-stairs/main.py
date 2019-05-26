"""
    1st appraoch: bottom-up iterative

	Time 	O(n) iterate from 1 to N
	Space	O(n) for the array
	12ms beats 98.53%
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1]
        for i in range(2, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]


"""
    2nd approach: top-down recursive
    - use a hashtable to avoid redundant calculation
	
    Time O(n)		duplicates are avoided so only the unseen numbers go through the calculations
	Space O(2n)	n for hashtable, n for recursive callstack
	20 ms, faster than 66.37%
"""


class Solution(object):

    def __init__(self):
        self.cache = {}
        self.cache[0] = 1
        self.cache[1] = 1

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.cache:
            return self.cache[n]
        temp = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.cache[n] = temp
        return temp
