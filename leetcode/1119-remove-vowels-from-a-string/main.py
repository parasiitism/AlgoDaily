"""
    1st approach: hashset

    Time    O(n)
    Space   O(n)
    20 ms, faster than 43.91%
"""


class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        res = ''
        for c in S:
            if c not in vowels:
                res += c
        return res
