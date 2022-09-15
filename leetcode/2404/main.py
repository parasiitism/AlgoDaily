"""
    hashtable

    Time    O(N)
    Space   O(N)
    743 ms, faster than 50.00%
"""


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        ctr = defaultdict(int)
        max_count = 0
        res = -1
        for i in range(len(nums)):
            x = nums[i]
            if x % 2 == 1:
                continue
            ctr[x] += 1
            if ctr[x] > max_count:
                max_count = ctr[x]
                res = x
            elif ctr[x] == max_count:
                res = min(res, x)
        return res
