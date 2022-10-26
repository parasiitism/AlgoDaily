"""
    Binary search
    - the optimal cost must lye between the min(A) and max(A) <- it's a covex function potentially
    - so we can do binary search by comparing the cost(x) and cost(x+1) like the way we do leetcode162: Find Peak Element/local minmax

    Time    O(Nlog(max(A) - min(A)))
    Space   O(1)
    5728 ms, faster than 7.69%
"""


class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:

        def find_cost(target):
            return sum(abs(x - target) * c for x, c in zip(nums, costs))

        L, R = min(nums), max(nums)
        res = find_cost(L)
        while L < R:
            M = (L + R) // 2
            c1, c2 = find_cost(M), find_cost(M + 1)
            res = min(c1, c2)
            if c1 <= c2:
                R = M
            else:
                L = M + 1
        return res
