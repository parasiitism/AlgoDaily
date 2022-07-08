from collections import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    classic question: spiral matrix traverse
    - similar to leetcode 59

    Time    O(RC)
    Space   O(RC)
    1686 ms, faster than 89.94%
"""


class Solution:
    def spiralMatrix(self, R: int, C: int, head: Optional[ListNode]) -> List[List[int]]:
        res = []
        for _ in range(R):
            temp = C * [-1]
            res.append(temp)
        q = deque()
        cur = head
        while cur != None:
            q.append(cur.val)
            cur = cur.next

        top = 0
        right = C - 1
        bottom = R - 1
        left = 0

        while top <= bottom and left <= right:
            # go right
            for j in range(left, right+1):
                res[top][j] = q.popleft() if len(q) > 0 else -1
            top += 1
            # go down
            for i in range(top, bottom+1):
                res[i][right] = q.popleft() if len(q) > 0 else -1
            right -= 1
            # go left
            # top has been +1 previously, so bottom must be >= new top in order to traverse correctly
            if top <= bottom:
                for j in range(right, left-1, -1):
                    res[bottom][j] = q.popleft() if len(q) > 0 else -1
                bottom -= 1
            # go up
            # left has been +1 previously, so right must be >= new top in order to traverse correctly
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res[i][left] = q.popleft() if len(q) > 0 else -1
                left += 1

        return res
