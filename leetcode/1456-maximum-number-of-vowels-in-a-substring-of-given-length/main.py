"""
    1st: sliding window

    Time    O(N)
    Space   O(1)
    468 ms, faster than 100.00%
"""


class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        cur = 0
        for i in range(len(s)):
            c = s[i]
            if c in 'aeiou':
                cur += 1
            if i >= k:
                left = s[i-k]
                if left in 'aeiou':
                    cur -= 1
            res = max(res, cur)
        return res
