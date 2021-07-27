"""
    1st: stack
    - learned from others

    ref:
    - https://leetcode.com/problems/number-of-visible-people-in-a-queue/discuss/1359707/JavaC%2B%2BPython-Stack-Solution-Next-Greater-Element

    Time    O(N)
    Space   O(N)
    1244 ms, faster than 55.93%
"""


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        N = len(heights)
        res = N * [0]

        # store the idx i
        stack = []

        for i in range(N):
            h = heights[i]

            # people on the left sees this person, so heights[left] += 1
            # because this person blocks left's view, left won't be seeing right view anymore, we can remove left
            while len(stack) > 0 and heights[stack[-1]] <= h:
                left = stack[-1]
                res[left] += 1
                stack.pop()

            # the last person on the left sees this person, so heights[left] += 1
            if len(stack) > 0:
                left = stack[-1]
                res[left] += 1

            stack.append(i)
        return res
