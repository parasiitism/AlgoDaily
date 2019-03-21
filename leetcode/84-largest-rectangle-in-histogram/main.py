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
            cnt = 1
            for j in range(i, -1, -1):
                maxheight = min(maxheight, heights[j])
                temp = maxheight * cnt
                res = max(res, temp)
                cnt += 1
        return res


print(Solution().largestRectangleArea([]))
print(Solution().largestRectangleArea([2]))
print(Solution().largestRectangleArea([2, 1]))
print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(Solution().largestRectangleArea([12, 23, 12, 25, 3, 16]))

print("-----")


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int

        2nd approach: stack <= learned from others 
        - use a stack to store the indeces where the corresponding height can create a potential largest retangle

        ref:
        - https://www.youtube.com/watch?v=ZmnqCZp9bBs

        Time	O(n)
        Space	O(1)
        168 ms, faster than 5.14% <= the code is similar to the one beats 100% so i am not sure why so slow
        """
        res = 0
        if len(heights) == 0:
            return 0
        stack = [-1, 0]
        # iterate  through the list
        for i in range(1, len(heights)):
            cur = heights[i]
            if cur >= heights[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 1 and cur < heights[stack[-1]]:
                    idx = stack.pop()
                    # i-stack.peek()-1 is the width
                    temp = heights[idx] * (i-stack[-1]-1)
                    res = max(res, temp)
                stack.append(i)
        while len(stack) > 1:
            idx = stack.pop()
            temp = heights[idx] * (len(heights)-stack[-1]-1)
            res = max(res, temp)
        return res


print(Solution().largestRectangleArea([]))
print(Solution().largestRectangleArea([2]))
print(Solution().largestRectangleArea([2, 1]))
print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(Solution().largestRectangleArea([12, 23, 12, 25, 3, 16]))
