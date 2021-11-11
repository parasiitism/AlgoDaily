"""
    1st: lower bound binary search
    - search the smallest fragment that can fit in all the products

    Time    O(NlogN)
    Space   O(1)
    2648 ms, faster than 84.62% 
"""


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 1
        right = max(quantities)
        while left < right:
            mid = (left + right)//2
            if self.canFitIn(n, quantities, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def canFitIn(self, n, quantities, mid):
        potentialStoresCount = 0
        for q in quantities:
            a = q // mid
            b = q % mid
            potentialStoresCount += a
            if b > 0:
                potentialStoresCount += 1
        return potentialStoresCount <= n
