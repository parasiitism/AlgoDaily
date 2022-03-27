"""
    1st: array
    - deduplicate
    - count the peaks and dips

    Time    O(N)
    Space   O(N)
    40 ms, faster than 100.00%
"""


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)):
            x = nums[i]
            if i == 0:
                arr.append(x)
            else:
                p = nums[i-1]
                if x != p:
                    arr.append(x)
        res = 0
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1] or arr[i-1] > arr[i] < arr[i+1]:
                res += 1
        return res
