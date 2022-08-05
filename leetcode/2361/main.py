"""
    DP
    - an advanced version of
        - Maximum Subarray
        - Maximum Product Subarray

    Time    O(N)
    Space   O(N)
    2137 ms, faster than 100.00%
"""


class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular)
        regular_total = 0
        express_total = expressCost
        res = n * [0]
        for i in range(n):
            _regular_total = min(
                regular_total + regular[i], express_total + express[i])
            _express_total = min(
                regular_total + regular[i] + expressCost, express_total + express[i])

            regular_total, express_total = _regular_total, _express_total

            res[i] = min(regular_total, express_total)
        return res
