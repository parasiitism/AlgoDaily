from collections import *

"""
    hashtable + sort

    Time    O(NlogD + NlogN)
    Space   O(N)
    1038 ms, faster than 100.00%
"""


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ht = defaultdict(list)
        for x in nums:
            temp = x
            digit_sum = 0
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            ht[digit_sum].append(x)
        res = -1
        for key in ht:
            arr = ht[key]
            arr.sort(key=lambda x: -x)
            if len(arr) >= 2:
                res = max(res, arr[0] + arr[1])
        return res
