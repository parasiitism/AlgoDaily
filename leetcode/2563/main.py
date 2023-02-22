from bisect import *

"""
    1st: binary index tree

    Time    O(NlogN) 3134 ms Beats 36.36%
    Space   O(N)
"""
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sorted_num = list(sorted(set(nums)))
        rank = { sorted_num[i]: i for i in range(len(sorted_num))}
        bit = BIT(len(rank))
        for x in nums:
            index = rank[x]
            bit.update(index, 1)
        res = 0
        for i in range(len(nums)):
            x = nums[i]
            bit.update(rank[x], -1)
            # lower <= partner+x <= upper
            # lower - x <= partner <= upper - x
            partner_left = lower - x
            partner_right = upper - x
            left = bisect_left(sorted_num, partner_left)
            right = bisect_right(sorted_num, partner_right) - 1
            res += bit.getRangeSum(left, right)
        return res


class BIT(object):
    def __init__(self, n):
        self.fenwickTree = (n+1) * [0]
    def update(self, i, val):
        j = i + 1
        while j < len(self.fenwickTree):
            self.fenwickTree[j] += val
            j += j & -j
    def getSum(self, i):
        total_sum = 0
        j = i + 1
        while j > 0:
            total_sum += self.fenwickTree[j]
            j -= j & -j
        return total_sum
    def getRangeSum(self, i, j):
        return self.getSum(j) - self.getSum(i-1)

"""
    2nd: binary search
    - actuall the order of nums doesn't matter

    Time    O(NlogN) 918 ms Beats 62.62%
    Space   O(N)
"""
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            x = nums[i]
            partner_left = lower - x
            partner_right = upper - x
            left = bisect_left(nums, partner_left, i+1)
            right = bisect_right(nums, partner_right, i+1)
            res += right - left
        return res