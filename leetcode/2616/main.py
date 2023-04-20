"""
    Sort + binary search

    idea:
    
    e.g.1
    [1, 1, 2, 3, 7, 10], p=2
    ----  ----
    The result is max(0, 1) = 1

    e.g.2
    [1, 10, 30, 33, 41, 43, 44, 45, 100, 102, 110], p=3
                    ------  ------  --------
    The result is max(2, 1, 2) = 2

    Time    O(NlogN)
    Space   O(N) the A. It can be O(1) if we sort the original array 
"""


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        A = sorted(nums)
        n = len(A)
        left = 0
        right = A[n-1] - A[0]
        while left < right:
            mid = (left + right)//2

            count = 0
            i = 1
            while i < n:
                diff = A[i] - A[i-1]
                if diff <= mid:
                    count += 1
                    i += 1
                i += 1

            if count >= p:
                right = mid
            else:
                left = mid + 1
        return left
