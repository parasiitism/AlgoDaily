"""
    1st approach: stack
    - similar to lc1614
	1. for each add, push to stack
	2. for each close and no counterpart in stack, result++
	3. result = res + len(stack)

	Time	O(n)
	Space	O(n)
    20 ms, faster than 96.69%
"""


class Solution(object):
    def minAddToMakeValid(self, S):
        opens = 0
        closes = 0
        for c in S:
            if c == '(':
                opens += 1
            else:
                if opens > 0:
                    opens -= 1
                else:
                    closes += 1
        return opens + closes


a = "())"
print(Solution().minAddToMakeValid(a))

a = "((("
print(Solution().minAddToMakeValid(a))

a = "()"
print(Solution().minAddToMakeValid(a))

a = "()))(("
print(Solution().minAddToMakeValid(a))

print("------------------------")

"""
    followup: we also include {} and []
    therefore 3 types:
    - (), {}, []
"""


class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type S: str
        :rtype: int
        """
        if len(s) == 0:
            return True
        stack = []
        m = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        extra_closes = 0
        for c in s:
            if c in '{[(':
                stack.append(c)
            elif c in m:
                if len(stack) > 0 and stack[-1] == m[c]:
                    stack.pop()
                else:
                    extra_closes += 1
        return len(stack) + extra_closes


a = "())"
print(Solution().minAddToMakeValid(a))

a = "((("
print(Solution().minAddToMakeValid(a))

a = "()"
print(Solution().minAddToMakeValid(a))

a = "()))(("
print(Solution().minAddToMakeValid(a))

a = "()){}"
print(Solution().minAddToMakeValid(a))

a = "((({{}"
print(Solution().minAddToMakeValid(a))

a = "(){]"
print(Solution().minAddToMakeValid(a))

a = "()))(({]]}}"
print(Solution().minAddToMakeValid(a))
