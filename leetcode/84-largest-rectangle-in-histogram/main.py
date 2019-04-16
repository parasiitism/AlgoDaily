import sys


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int

        1st approach: brute force
        - for each bar, calculate the height from the current index to the index 0

        Time	O(n^2)
        Space	O(1)
        TLE
        """
        res = 0
        for i in range(len(heights)):
            maxheight = sys.maxsize
            for j in range(i, -1, -1):
                maxheight = min(maxheight, heights[j])
                temp = maxheight * (i-j+1)
                res = max(res, temp)
        return res


print(Solution().largestRectangleArea([]))
print(Solution().largestRectangleArea([2]))
print(Solution().largestRectangleArea([2, 1]))
print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(Solution().largestRectangleArea([12, 23, 12, 25, 3, 16]))

print("----------")


"""
    2nd approach: stack <= learned from others 
    - use a stack to store the indeces where the corresponding height can create a potential largest retangle

    ref:
    - https://www.youtube.com/watch?v=ZmnqCZp9bBs

    Time	O(n)
    Space	O(n)
    100 ms, faster than 31.99% 
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        res = 0
        # begining with -1, such that we can calculate the range, i - stack[-1][0] - 1, easier
        # (index, height)
        stack = [(-1, 0)]
        for i in range(len(heights)):
            cur = heights[i]
            if cur > stack[-1][1]:
                # if current height is taller, append to the stack
                stack.append((i, cur))
            else:
                # pop the stack if the items which is > cur height
                while stack[-1][1] > cur:
                    popIdx, popH = stack.pop()
                    width = i - stack[-1][0] - 1
                    area = popH * width
                    res = max(res, area)
                # put the current item to the array
                stack.append((i, cur))
        # if the stack is not empty, pop the items
        while len(stack) > 1:
            popIdx, popH = stack.pop()
            width = len(heights) - stack[-1][0] - 1
            area = popH * width
            res = max(res, area)
        return res


print(Solution().largestRectangleArea([]))
print(Solution().largestRectangleArea([2]))
print(Solution().largestRectangleArea([2, 1]))
print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(Solution().largestRectangleArea([12, 23, 12, 25, 3, 16]))

print("----------")
