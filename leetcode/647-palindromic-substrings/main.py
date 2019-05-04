"""
    naive approach:
    generate all the substrings and check

    Time    O(n^3)
    Space   O(1)
"""

"""
    1st approach: expand from center like lc5

    Time    O(n^2)
    Space   O(1)
    132 ms, faster than 51.55%
"""


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            count1 = self.explore(s, i, i)
            count2 = self.explore(s, i-1, i)
            res += count1 + count2
        return res

    def explore(self, s, left, right):
        if left < 0:
            return 0
        if right+1 > len(s):
            return 0
        if s[left] != s[right]:
            return 0
        count = 1
        while left-1 >= 0 and right+1 < len(s) and s[left-1] == s[right+1]:
            left -= 1
            right += 1
            count += 1
        return count
