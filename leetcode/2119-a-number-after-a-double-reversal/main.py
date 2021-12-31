"""
    1st: string

    Time    O(N)
    Space   O(N)
    28 ms, faster than 80.00%
"""


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)
        num_ = int(s[::-1])
        s_ = str(num_)
        return len(s) == len(s_)
