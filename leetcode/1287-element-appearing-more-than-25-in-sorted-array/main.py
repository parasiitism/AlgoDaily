from collections import defaultdict

"""
    1st: hashtable
    - record count of each number
    - afterall, check if there is one number appears more than 25%

    Time        O(N)
    Space       O(N)
    80 ms, faster than 56.29%
"""


class Solution(object):
    def findSpecialInteger(self, arr):
        ht = defaultdict(int)
        for x in arr:
            ht[x] += 1
        target = len(arr) / 4
        for key in ht:
            if ht[key] > target:
                return key


"""
    2nd: binary search
    - for each number, binary search its upper bound
    - and check if the range is more than 25% of the length of the input array

    Time    O(NlogN)
    Space   O(1)
    128 ms, faster than 7.76%
"""


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if i == 0 or arr[i] != arr[i-1]:
                right = self.upperBsearch(arr, arr[i], i)
                diff = right - i
                if diff > len(arr) // 4:
                    return arr[i]

    def upperBsearch(self, nums: List[int], target: int, start: int) -> int:
        left = start
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left
