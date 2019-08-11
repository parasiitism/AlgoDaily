"""
    1st approach: similar to 2 pointers
    - maintain 2 arrays which represent 2 sides of a mountain
    - when arr[i] > arr[i-1], append left
    - when arr[i] < arr[i-1], append right
    - when arr[i] == arr[i-1], reset the left and right
    - need to take care of the pivot point, e.g. 3,4,5,2,1,x. When x is > arr[i-1] and x > right[-1], reset the left and right

    Time    O(n)
    Space   O(n)
    164 ms, faster than 24.55%
"""


class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        left = [A[0]]
        right = []
        res = 0
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                if len(right) > 0 and A[i] > right[-1]:
                    left = [right[-1]]
                    right = []
                if A[i] > left[-1]:
                    left.append(A[i])
            elif A[i] < A[i-1]:
                right.append(A[i])
            else:
                left = [A[i]]
                right = []
            if len(left) > 1 and len(right) > 0:
                res = max(res, len(left) + len(right))

        if len(left) > 1 and len(right) > 0:
            res = max(res, len(left) + len(right))

        return res if res >= 3 else 0
