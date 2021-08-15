"""
    1st: 2 arrays min max
    - the idea is similar to quick sort
    - for a number at any index
        - if every element on the left is smaller than it, it can be found (cos binary search can remove the elements on the left)
        - if every element on the right is larger than it, it can be found
    - therefore, we just have to see if the current is at the right index(pivot in quick sort)

    Time    O(N)
    Space   O(N)
    607 ms, faster than 100.00%
"""


class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        prefix = n * [False]
        preifx_max = nums[0]
        suffix_min = nums[-1]
        for i in range(n):
            prefix[i] = preifx_max <= nums[i]
            preifx_max = max(preifx_max, nums[i])
        for i in range(n-1, -1, -1):
            suffix_min = min(suffix_min, nums[i])
            if prefix[i] and nums[i] <= suffix_min:
                res += 1
        return res
