"""
    1st approach:
    - slice substring
    - for each char, slic the substring and compare
    Time		O(n)
    Space		O(1)
    544ms beats 100%
    3may2019
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                chop = haystack[i:i+len(needle)]
                if chop == needle:
                    return i
        return -1
