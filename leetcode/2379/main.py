"""
    sliding window
    - count the W within the sliding window

    Time    O(N)
    Space   O(1)
    58 ms, faster than 60.00%
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        window_white_count = 0
        res = n
        for i in range(n):
            c = blocks[i]
            if c == 'W':
                window_white_count += 1
            if i-k >= 0:
                if blocks[i-k] == 'W':
                    window_white_count -= 1
            if i >= k-1:
                res = min(res, window_white_count)
        return res
