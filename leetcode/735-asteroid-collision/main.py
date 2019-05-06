"""
    1st approach: stack
    - if positive, just put into stack
    - if negative:
      1. - pop the stack if abs(num) is larger than the top item in the stack
         - if the stack becomes empty, append the num into the res array
      2. pop the stack if abs(num) == stack[-1], skip appending

    Time    O(n)
    Space   O(n)
    92 ms, faster than 33.38%
"""


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = []
        stack = []
        for num in asteroids:
            if num >= 0:
                stack.append(num)
            else:
                # pop the smaller items from the stack
                while len(stack) > 0 and abs(num) > abs(stack[-1]):
                    stack.pop()
                # same size asteroid collide
                if len(stack) > 0 and abs(num) == abs(stack[-1]):
                    stack.pop()
                    continue
                # append num to res if empty or > stack[-1]
                if len(stack) == 0 or abs(num) > abs(stack[-1]):
                    res.append(num)
        return res + stack
