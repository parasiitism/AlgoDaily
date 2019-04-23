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
    LTE 119/120 (python only)
"""


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rStr = s[::-1]
        for i in range(len(s)):
            temp = rStr[:i] + s
            if self.isPalindrome(temp):
                return temp
        return ""

    """
    # it takes completely O(n), it's too slow
    def isPalindrome(self, s):
        r = s[::-1]
        return r == s
    """

    # it takes less than O(n) because we dont necessarily need to iterate the whole array
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

a = "ccab"
print(Solution().shortestPalindrome(a))

a = "a"
print(Solution().shortestPalindrome(a))

a = ""
print(Solution().shortestPalindrome(a))

print("---------------------")

"""
    learned from others:

    e.g. "abacde"
    s          abacde
    --------------------------
    r[0:]      edcaba    Nope
    r[1:]    e|dcaba     Nope
    r[2:]   ed|caba      Nope
    r[3:]  edc|aba       Yes! the string starts with "aba", so the result is edc + abacde

    ref:
    - https://leetcode.com/problems/shortest-palindrome/discuss/60099/AC-in-288-ms-simple-brute-force

    Time    O(n^2)
    Space   O(n)
    
"""


class Solution(object):
    def shortestPalindrome(self, s):
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s


a = "aacecaaa"
print(Solution().shortestPalindrome(a))

a = "abcd"
print(Solution().shortestPalindrome(a))

a = "ccab"
print(Solution().shortestPalindrome(a))

a = "a"
print(Solution().shortestPalindrome(a))

a = ""
print(Solution().shortestPalindrome(a))
