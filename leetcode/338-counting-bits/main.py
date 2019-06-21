"""
    1st approach: brute force
    - count the set for each number from 0 to num

    Time    O(nlogn)
    Space   O(n)
    196 ms, faster than 9.56%
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num+1):
            temp = self.countSet(i)
            res.append(temp)
        return res

    def countSet(self, num):
        count = 0
        while num > 0:
            if num & 1 == 1:
                count += 1
            num >>= 1
        return count


s = Solution()
print(s.countBits(4))
print(s.countBits(10))
print("-----")

"""
    2nd approach: dynamic programming
    
    e.g.1 even
    12 = 1100
    6  = 110
    - the prefix of an even number is the same with the half of it
    - the suffix is the extra zero

    e.g.2
    605 = 1001011101
    302 = 100101110
    - the prefix of an even number is the same with the half of it
    - the suffix is the extra one

    so it means that we can use the previous result for calculation

    Time    O(n)
    Space   O(n)
    96 ms, faster than 35.98%
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = (num + 1) * [0]
        for i in range(num+1):
            dp[i] = dp[i//2] + i % 2
        return dp


s = Solution()
print(s.countBits(4))
print(s.countBits(10))
print("-----")
