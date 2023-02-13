"""
    hashtable
    
    Time    O(N)
    Space   O(B)
"""


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        pfs = 0
        res = 0
        for i in range(1, n+1):
            if i in banned:
                continue
            pfs += i
            if pfs > maxSum:
                break
            res += 1
        return res
