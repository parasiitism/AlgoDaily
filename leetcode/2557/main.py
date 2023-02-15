"""
    binary search
    - this question is exactly the same as leetcode2554, the difference is the scale
    - the idea is to binary-search the upper bound where (1+n)n/2 - banned <= maxSum

    Time    O(Blog(10**9))
    Space   O(1)
"""


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        left = 0
        right = n + 1
        while left < right:
            mid = (left + right)//2
            cnt = mid

            total = mid*(mid+1)//2
            for x in banned:
                if x <= mid:
                    cnt -= 1
                    total -= x

            if maxSum >= total:
                left = mid + 1
            else:
                right = mid
        return left - 1 - sum(x <= left for x in banned)
