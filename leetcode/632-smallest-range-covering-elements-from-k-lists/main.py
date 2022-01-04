from bisect import *
from heapq import *


"""
    1st: binary search + N pointers
    - maintain a sorted list with a number from every list
    - pop the smallest from the sorted list and add its successor in 
    - then calculate the min and max, and update the result if necessary

    e.g.
    [4, 10, 15, 24, 26]
     ^
    [0, 9, 12, 20]
     ^
    [5, 18, 22, 30]
    ^
    sorted_list = [0, 4, 5] <- diff = 5
--------------------------------------------------------
    [4, 10, 15, 24, 26]
     ^
    [0, 9, 12, 20]
        ^
    [5, 18, 22, 30]
     ^
    sorted_list = [4, 5, 9] <- diff = 5
--------------------------------------------------------
    [4, 10, 15, 24, 26]
        ^
    [0, 9, 12, 20]
        ^
    [5, 18, 22, 30]
     ^
    sorted_list = [5, 9, 10] <- diff = 5
--------------------------------------------------------
    [4, 10, 15, 24, 26]
        ^
    [0, 9, 12, 20]
        ^
    [5, 18, 22, 30]
        ^
    sorted_list = [9, 10, 18] <- diff = 9
--------------------------------------------------------
    and so on....

    Time    O(RCR)
    Space   O(R)
    396 ms, faster than 10.54%
"""


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        N = len(nums)
        sorted_list = []  # (num, r, c)
        for r in range(N):
            x = nums[r][0]
            idx = self.upperBsearch(sorted_list, x)
            sorted_list.insert(idx, (x, r, 0))

        left = sorted_list[0][0]
        right = sorted_list[-1][0]
        diff = right - left

        while len(sorted_list) == N:
            _, r, c = sorted_list.pop(0)
            _c = c + 1
            if _c < len(nums[r]):
                x = nums[r][_c]
                idx = self.upperBsearch(sorted_list, x)
                sorted_list.insert(idx, (x, r, _c))
                if sorted_list[-1][0] - sorted_list[0][0] < diff:
                    left = sorted_list[0][0]
                    right = sorted_list[-1][0]
                    diff = right - left
        return [left, right]

    def upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid][0]:
                left = mid + 1
            else:
                right = mid
        return right


"""
    2nd: minheap
    - optimize the 1st approach
    - we can just
        - keep track of the min with a minheap
        - keep track of the max whenever we push a new item in the minheap
    
    Time    O(RClogR)
    Space   O(R)
    248 ms, faster than 35.71%
"""


class Solution(object):
    def smallestRange(self, nums):
        N = len(nums)
        res = [-(2**32), 2**32]

        minheap = []
        right = res[0]
        for r in range(N):
            x = nums[r][0]
            heappush(minheap, (x, r, 0))
            right = max(right, x)

        while len(minheap) == N:
            left, r, c = heappop(minheap)

            if right - left < res[1] - res[0]:
                res = [left, right]

            _c = c + 1
            if _c < len(nums[r]):
                x = nums[r][_c]
                right = max(right, x)
                heappush(minheap, (x, r, _c))
        return res
