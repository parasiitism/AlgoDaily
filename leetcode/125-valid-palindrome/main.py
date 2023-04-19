"""
    1st: classic approach
	- 2 pointers: 1 from the front, 1 from the back, and check if s[i] == s[j]

    Time    O(N)
    Space   O(1)
    52 ms, faster than 47.60%
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not self.isAlphanumeric(s[left]):
                left += 1
            while left < right and not self.isAlphanumeric(s[right]):
                right -= 1
            if left <= right and s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    def isAlphanumeric(self, c):
        return 0 <= ord(c) - ord('a') < 26 or 0 <= ord(c) - ord('0') < 10


"""
    2nd: similar to 1st but concise

    Time    O(N)
    Space   O(1)
    48 ms, faster than 68.75%
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            elif s[i].isalnum():
                j -= 1
            elif s[j].isalnum():
                i += 1
            else:
                i += 1
                j -= 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        left, right = 0, len(s) - 1
        while left < right:
            if self.is_alpha_numeric(s[left]) and self.is_alpha_numeric(s[right]):
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            elif self.is_alpha_numeric(s[left]):
                right -= 1
            elif self.is_alpha_numeric(s[right]):
                left += 1
            else:
                left += 1
                right -= 1
        return True

    def is_alpha_numeric(self, c):
        return (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9')


"""
    3rd: recursion

    Time    O(N)
    Space   O(1)
    64 ms, faster than 27.95%
"""


class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        return self.isValid(s, 0, len(s)-1)

    def isValid(self, s, i, j):
        if i >= j:
            return True
        if s[i].isalnum() and s[j].isalnum():
            if s[i] == s[j]:
                return self.isValid(s, i+1, j-1)
            return False
        elif s[i].isalnum():
            return self.isValid(s, i, j-1)
        elif s[j].isalnum():
            return self.isValid(s, i+1, j)
        return self.isValid(s, i+1, j-1)
