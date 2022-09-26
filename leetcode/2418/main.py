"""
    sort

    Time    O(NlogN)
    Space   O(N)
    287 ms, faster than 41.67%
"""


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        pairs = []
        for i in range(n):
            x = names[i]
            h = heights[i]
            pairs.append((h, x))
        pairs.sort(key=lambda x: -x[0])
        res = []
        for _, name in pairs:
            res.append(name)
        return res
