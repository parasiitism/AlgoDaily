"""
    1st: stack
    - based on the concept of The Next Greater Element

    ref:
    - https://leetcode.com/problems/number-of-visible-people-in-a-queue/discuss/1359707/JavaC%2B%2BPython-Stack-Solution-Next-Greater-Element

    Time    O(N)
    Space   O(N)
    1299 ms, faster than 44.55% 
"""


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        N = len(heights)
        res = N * [0]

        # store the idx i
        stack = []

        for i in range(N):
            h = heights[i]

            # people on the left see this person, so heights[left] += 1
            #
            while len(stack) > 0 and heights[stack[-1]] <= h:
                left = stack[-1]
                res[left] += 1
                stack.pop()

            # most recent on the left see this person, so heights[left] += 1
            if len(stack) > 0:
                left = stack[-1]
                res[left] += 1

            stack.append(i)
        return res
