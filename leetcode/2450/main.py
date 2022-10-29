"""
    Math
    - each digit has 2 possibilities: 0 and 1
    - look at how many digits will be flipped

    Time    O(1)
    Space   O(1)
"""


class Solution:
    def countDistinctStrings(self, s: str, k: int) -> int:
        n = len(s)
        res = 2**(n - k + 1)
        res %= 10**9 + 7
        return res
