"""
    1st: bottom-up DP

    Time    O(n)
    Space   O(n)
    12ms beats 90.27%
"""


class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 1]
        if n < 3:
            return dp[n]
        for i in range(3, n+1):
            dp.append(dp[i-1]+dp[i-2]+dp[i-3])
        return dp[-1]


"""
    2nd: top-down recursion + hashtable

    Time    O(n)
    Space   O(n)
    16 ms, faster than 69.55%
"""


class Solution(object):

    def __init__(self):
        self.ht = {}

    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if n in self.ht:
            return self.ht[n]
        temp = self.tribonacci(
            n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        self.ht[n] = temp
        return temp
