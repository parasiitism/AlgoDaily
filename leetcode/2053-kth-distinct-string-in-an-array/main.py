from collections import *

"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
    60 ms, faster than 50.00% 
"""


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        j = 0
        for i in range(len(arr)):
            if counter[arr[i]] == 1:
                j += 1
                if j == k:
                    return arr[i]
        return ''
