"""
    1st: sort + hashtable

    Time    O(NlogN)
    Space   O(N)
    360 ms, faster than 93.60%
"""


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))
        ht = {}
        for i in range(len(temp)):
            ht[temp[i]] = i+1
        res = []
        for x in arr:
            res.append(ht[x])
        return res
