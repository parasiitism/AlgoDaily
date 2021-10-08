"""
    1st: greedy
    - whenever the current element a is bigger than the previous element,
        we need at lease a - prev operations to make this difference.
    - we accumulate the total number of the operations

    Time    O(N)
    Space   O(1)
    800 ms, faster than 76.37%
"""


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res, prev = 0, 0
        for x in target:
            res += max(x - prev, 0)
            prev = x
        return res
