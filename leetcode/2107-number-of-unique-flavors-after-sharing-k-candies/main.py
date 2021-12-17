from collections import *

"""
    1st: sliding window + hashtable
    - counter the characters outside the sliding window

    Time    O(N)
    Space   O(N)
    875 ms, faster than 100.00%
"""


class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        counter = Counter(candies)
        res = 0
        for i in range(len(candies)):
            c = candies[i]

            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]

            if i >= k:
                p = candies[i-k]
                if p not in counter:
                    counter[p] = 0
                counter[p] += 1

            if i >= k-1:
                res = max(res, len(counter))
        return res
