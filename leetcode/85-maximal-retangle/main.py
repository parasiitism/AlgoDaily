class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int

        classic approach: dynamic programming + max area within a histogram(leetcode 84)

        e.g.
        [
          [1,0,1,0,0],
          [1,0,1,1,1],
          [1,1,1,1,1],
          [1,0,0,1,0],
        ]

        for each row, we accumulate the ones on the grids on position in previous row and find the area of the current histogram
        [1,0,1,0,0] <- maxarea 1
        [2,0,2,1,1] <- maxarea 3
        [3,1,3,2,2] <- maxarea 6
        [4,0,0,3,0] <- maxarea 4

        therefore the answer is 6

        Time  O(n^2)
        Space O(n)
        380 ms, faster than 11.81%
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        retangle = None
        res = 0
        for arr in matrix:
            if retangle == None:
                # leetcode is bad at presenting the question ["1","0","1","0","0"] <- WTF
                retangle = [int(x) for x in arr]
            else:
                for j in range(len(arr)):
                    if arr[j] == '0':
                        retangle[j] = 0
                    else:
                        retangle[j] += 1
            area = self.largestRectangleArea(retangle)
            if area > res:
                res = area
        return res

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


a = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(Solution().maximalRectangle(a))
