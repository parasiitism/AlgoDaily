"""
    1st: top-down recursive
	- use a hashtable to avoid redundant calculation
	
    Time O(n)		duplicates are avoided so only the unseen numbers go through the calculations
	Space O(2n)	    n for hashtable, n for recursive callstack
	12 ms, faster than 98.77%
"""


class Solution(object):

    def __init__(self):
        self.m = {}

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 0:
            return 0
        elif N == 1:
            return 1
        if N in self.m:
            return self.m[N]
        temp = self.fib(N-1) + self.fib(N-2)
        self.m[N] = temp
        return temp


"""
    2nd: bottom-up iterative

	Time 	O(n) iterate from 1 to N
	Space	O(n) for the array
	0ms beats 100%
"""


class Solution(object):

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0, 1]
        for i in range(2, N+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[N]
