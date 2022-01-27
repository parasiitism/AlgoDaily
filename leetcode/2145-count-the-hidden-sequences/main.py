"""
    1st: binary search

    Time    O(NlogN)
    Space   O(1)
    3781 ms, faster than 16.67%
"""


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        smallest_start = self.bsearchSmallest(differences, lower, upper)
        largest_start = self.bsearchLargest(differences, lower, upper) - 1
        if lower <= smallest_start and largest_start <= upper:
            return largest_start - smallest_start + 1
        return 0

    def bsearchSmallest(self, differences, lower, upper):
        left = lower
        right = upper + 1
        while left < right:
            mid = (left + right)//2

            pfs = mid
            canFormSequence = 0
            for d in differences:
                pfs += d
                if pfs < lower:
                    canFormSequence = -1
                    break
                elif pfs > upper:
                    canFormSequence = 1
                    break

            if canFormSequence >= 0:
                right = mid
            else:
                left = mid + 1
        return left

    def bsearchLargest(self, differences, lower, upper):
        left = lower
        right = upper+1
        while left < right:
            mid = (left + right)//2

            pfs = mid
            canFormSequence = 0
            for d in differences:
                pfs += d
                if pfs < lower:
                    canFormSequence = -1
                    break
                elif pfs > upper:
                    canFormSequence = 1
                    break

            if canFormSequence <= 0:
                left = mid + 1
            else:
                right = mid
        return left
