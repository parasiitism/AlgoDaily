import sys

"""
    1st approach: sort

    e.g. [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]

    [0, 0, 1, 1, 1, 4, 4, 8, 9, 9] <- sorted Array
     3  7  2  4  9  6  8  1  0  5  <- corresponding index

    when we iterate through the array, the maxRamp must be the correspondingIndex - minIdx that we saw previously

    Time    O(nlogn)
    Space   O(n)
    384 ms, faster than 33.74%
"""


class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sortedArr = []
        for i in range(len(A)):
            a = A[i]
            sortedArr.append((a, i))
        sortedArr = sorted(sortedArr)

        maxRamp = 0
        minIdx = sys.maxsize
        for a, i in sortedArr:
            ramp = i - minIdx
            maxRamp = max(maxRamp, ramp)
            minIdx = min(minIdx, i)
        return maxRamp


a = [2, 1]
print(Solution().maxWidthRamp(a))

a = [1, 2]
print(Solution().maxWidthRamp(a))

a = [6, 0, 8, 2, 1, 5]
print(Solution().maxWidthRamp(a))

a = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
print(Solution().maxWidthRamp(a))

print("-----")

"""
    2nd approach: binary search

    e.g. [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]

    [0, 0, 1, 1, 1, 4, 4, 8, 9, 9] <- sorted Array
     3  7  2  4  9  6  8  1  0  5  <- corresponding index

    when we iterate through the array, the maxRamp must be the correspondingIndex - minIdx that we saw previously

    Time    O(nlogn) -> O(n^2) because python slicing takes O(k) instead of O(1)
    Space   O(n)
    LTE
"""


class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sortedArr = []
        for i in range(len(A)):
            a = A[i]
            idx = self.upperBsearch(sortedArr, a)
            sortedArr = sortedArr[:idx] + [(a, i)] + sortedArr[idx:]

        maxRamp = 0
        minIdx = sys.maxsize
        for a, i in sortedArr:
            ramp = i - minIdx
            maxRamp = max(maxRamp, ramp)
            minIdx = min(minIdx, i)
        return maxRamp

    def upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)/2
            if target >= nums[mid][0]:
                left = mid + 1
            else:
                right = mid
        return right


a = [2, 1]
print(Solution().maxWidthRamp(a))

a = [1, 2]
print(Solution().maxWidthRamp(a))

a = [6, 0, 8, 2, 1, 5]
print(Solution().maxWidthRamp(a))

a = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
print(Solution().maxWidthRamp(a))
