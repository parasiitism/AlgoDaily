"""
    1st approach: brute force

    Time    O(n^3)
    Space   O(1)
    LTE
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if self.isValid(sub):
                    res = max(res, j-i+1)
        return res

    def isValid(self, s):
        if len(s) == 0:
            return True
        openCount = 0
        for c in s:
            if c == '(':
                openCount += 1
            else:
                if openCount == 0:
                    return False
                else:
                    openCount -= 1
        return openCount == 0


a = "(()"
print(Solution().longestValidParentheses(a))

a = ")()())"
print(Solution().longestValidParentheses(a))

a = ")(()()))))(()()())"
print(Solution().longestValidParentheses(a))

a = "()(()"
print(Solution().longestValidParentheses(a))

print("---------------")


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = 0
        res = 0
        openCount = 0

        for i in range(len(s)):
            c = s[i]
            if c == '(':
                openCount += 1
            else:
                if openCount == 0:
                    cur = 0
                else:
                    openCount -= 1
                    cur += 2
                    res = max(res, cur)
        return res


a = "(()"
print(Solution().longestValidParentheses(a))

a = ")()())"
print(Solution().longestValidParentheses(a))

a = ")(()()))))(()()())"
print(Solution().longestValidParentheses(a))

a = "()(()"
print(Solution().longestValidParentheses(a))
