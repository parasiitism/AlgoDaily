"""
    1st approach: reverse and check

    Time    O(logn)
    Space   O(logn)
    48 ms, faster than 96.23%
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return s == s[::-1]


"""
    2nd approach: 2 pointers

    Time    O(logn)
    Space   O(logn)
    44 ms, faster than 97.70%
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
