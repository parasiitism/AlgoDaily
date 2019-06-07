"""
    1st approach: stack
    - similar to lc735
    - while k > 0 and we see the curNum is smaller, pop the stack

    corner cases:
    1. num="9",     k=1
    2. num="12345", k=1

    Time    O(n)
    Space   O(n)
    40 ms, faster than 53.77%
"""


class Solution(object):
    def removeKdigits(self, number, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        nums = []
        for c in number:
            nums.append(int(c))

        stack = []
        for num in nums:
            # pop the bigger items from the stack
            while k > 0 and len(stack) > 0 and num < stack[-1]:
                stack.pop()
                k -= 1
            # append num to the stack
            stack.append(num)
        # if k > 0, remove from the right
        # because e.g. 123456, k = 1
        # 12345 < 23456
        while k > 0:
            stack.pop()
            k -= 1
        # stringigy the stack
        res = ""
        for x in stack:
            if len(res) == 0 and x == 0:
                continue
            res += str(x)
        if len(res) == 0:
            return "0"
        return res


a = "1432219"
b = 3
print(Solution().removeKdigits(a, b))

a = "10200"
b = 1
print(Solution().removeKdigits(a, b))

a = "10"
b = 2
print(Solution().removeKdigits(a, b))

a = "1498543459"
b = 4
print(Solution().removeKdigits(a, b))

a = "9"
b = 1
print(Solution().removeKdigits(a, b))

a = "12345"
b = 1
print(Solution().removeKdigits(a, b))

a = "112"
b = 1
print(Solution().removeKdigits(a, b))
