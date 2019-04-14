"""
    questions to ask:
    - empty sttring? return ""
    - single character string? return that character
"""


"""
    1st approach:
    - reverse str
    - append the reveresed str to the original str character by character and check if the combo is a palindrome

    Time    O(n^2)
    Space   O(n)
    LTE 119/120
"""


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rStr = self.reverseStr(s)
        for i in range(len(s)):
            temp = rStr[:i] + s
            if self.isPalindrome(temp):
                return temp
        return ""

    def reverseStr(self, s):
        res = ""
        for c in s:
            res = c + res
        return res

    def isPalindrome(self, s):
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


a = "aacecaaa"
print(Solution().shortestPalindrome(a))

a = "abcd"
print(Solution().shortestPalindrome(a))

a = "a"
print(Solution().shortestPalindrome(a))

a = ""
print(Solution().shortestPalindrome(a))
