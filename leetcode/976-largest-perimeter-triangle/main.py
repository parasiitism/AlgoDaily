"""
    1st approach: sort + binary search similar to 3sum
    - when we have A + B, we are looking for the C that A + B > C

    Time    O(n^2logn)
    Space   O(1)
    LTE
"""


class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = sorted(A)
        res = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                bound = A[i] + A[j]
                idx = self.lowerBsearch(A, bound, j+1)
                if idx != j and 0 <= idx < len(A):
                    area = bound + A[idx]
                    res = max(res, area)
        return res

    def lowerBsearch(self, A, target, fromIdx):
        left = fromIdx
        right = len(A)
        while left < right:
            mid = (left + right)/2
            if target <= A[mid]:
                right = mid
            else:
                left = mid + 1
        return left - 1


"""
    2nd approach: sort
    - A + B > C

    Time    O(nlogn)
    Space   O(1)
    248 ms, faster than 27.00% 
"""


class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        A = sorted(A)
        for i in range(len(A)-2):
            if A[i] + A[i+1] > A[i+2]:
                area = A[i] + A[i+1] + A[i+2]
                res = max(res, area)
        return res


"""
    3rd approach: sort
    - A + B > C

    Time    O(nlogn)
    Space   O(1)
    180 ms, faster than 69.07%
"""


class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = sorted(A)
        for i in range(len(A)-3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
