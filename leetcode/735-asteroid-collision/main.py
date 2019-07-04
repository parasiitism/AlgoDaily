"""
    1st approach: stack
    - similar to lc402
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


a = [5, 10, -5]
print(Solution().asteroidCollision(a))

a = [8, -8]
print(Solution().asteroidCollision(a))

a = [10, 2, -5]
print(Solution().asteroidCollision(a))

print("-----")

"""
    2nd approach: stack same idea as 1st approach
    - similar to lc402
    - if positive, just put into stack
    - if negative:
      1. pop the stack if abs(num) is larger than the top positive item in the stack
      2. if the stack becomes empty or top item is negative, pile up the stack with the num
      3. pop the stack if abs(num) == stack[-1], skip appending

    Time    O(n)
    Space   O(n)
    88 ms, faster than 51.57%
"""


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for num in asteroids:
            if num >= 0:
                stack.append(num)
            else:
                # pop the smaller items from the stack
                while len(stack) > 0 and stack[-1] > 0 and abs(num) > stack[-1]:
                    stack.pop()
                # same size asteroid collide
                # e.g. [10,5,-5,-10,-3] dont put -10 onto the stack
                if len(stack) > 0 and stack[-1] > 0 and abs(num) == stack[-1]:
                    stack.pop()
                    continue
                # append num to res if empty or stack[-1] < 0
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(num)
        return stack


a = [5, 10, -5]
print(Solution().asteroidCollision(a))

a = [8, -8]
print(Solution().asteroidCollision(a))

a = [10, 2, -5]
print(Solution().asteroidCollision(a))
