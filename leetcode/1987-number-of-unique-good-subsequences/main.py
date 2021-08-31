"""
    1st: dynamic programming
    - similar to leetcode940
    - when we meet an 0, we can add the 0 to any sequences which end with 0 or 1
    - when we meet an 1, we can add the 1 to any sequences which end with 0 or 1, AND create a new sequence
    - at the end, dont forget the single 0 (if any)

    Time    O(N)
    Space   O(1)
    148 ms, faster than 100.00%
"""


class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        mod = 10**9 + 7
        endsWith0 = 0
        endsWith1 = 0
        has0 = 0
        for c in binary:
            if c == '0':
                endsWith0 = (endsWith0 + endsWith1) % mod
                has0 = 1
            else:
                endsWith1 = (endsWith0 + endsWith1 + 1) % mod
        return (endsWith0 + endsWith1 + has0) % mod
