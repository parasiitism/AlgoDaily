"""
    1st approach: math

    Time    O(n)
    Space   O(26)
    20 ms, faster than 67.08%
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ""
        alphbets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""
        while n > 0:
            n = n - 1  # we are going to get the index, so n-1
            mod = n % 26
            res = alphbets[mod] + res
            n /= 26
        return res


print(Solution().convertToTitle(1))
print(Solution().convertToTitle(26))
print(Solution().convertToTitle(28))
print(Solution().convertToTitle(676))
