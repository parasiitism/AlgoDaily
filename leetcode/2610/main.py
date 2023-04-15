"""
    hashtable

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ht = Counter(nums)
        res = []
        while len(ht) > 0:
            row = []
            keys = list(ht.keys())
            for k in keys:
                row.append(k)
                ht[k] -= 1
                if ht[k] == 0:
                    del ht[k]
            res.append(row)
        return res
