from collections import defaultdict
from typing import List

"""
    1st: dyanamic programming with hashtable
    - use a hashtable to store the { distinct number : max length of a sequence }

    e.g.
    [1, 5, 7, 8, 5, 3, 4, 2, 1], -2
     1  1  1  1  2  3  1  2  4       <- for each number, find if ht[x-dff] exists and update ht[x] with the max length of a sequence
    
    Time    O(N)
    Space   O(N)
    664 ms, faster than 26.39%
"""


class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        ht = defaultdict(int)
        for x in arr:
            if x - diff not in ht:
                ht[x] = 1
            else:
                ht[x] = max(ht[x], ht[x-diff] + 1)
        return max(ht.values())
