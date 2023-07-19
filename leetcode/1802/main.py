"""
    upper-bound binary search
    - the implement is not annoying, there 2 cases we need to consider
        - e.g. [8,9,10,11,10,9,8,7] where we need to count from 8<-10 and 10->7
        - e.g. [1,1,1,1,2,3,4,5,4,3,2,1,1,1] where we need to also count the ones

    learned from here
    - https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array/solution/by-powcai-e006/
    
    Time    O(NlogM) M: maxSum
    Space   O(1)
"""


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left = 1
        right = maxSum + 1
        while left < right:

            mid = (left + right) // 2
            sum_L = self.sumAll(mid - 1, index)
            sum_R = self.sumAll(mid - 1, n - index - 1)

            if sum_L + mid + sum_R <= maxSum:
                left = mid + 1
            else:
                right = mid

        return left - 1

    def sumAll(self, peak, length):
        if length == 0:
            return 0
        dip = max(1, peak - length + 1)
        remain = peak - dip + 1
        ones = length - remain
        return (peak - dip + 1) * (peak + dip) // 2 + ones
