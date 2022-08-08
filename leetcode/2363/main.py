"""
    hashtable + sort
    
    Time    O(NlogN)
    Space   O(N)
    230 ms, faster than 16.67%
"""


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ht = defaultdict(int)
        for v, w in items1:
            ht[v] += w
        for v, w in items2:
            ht[v] += w
        res = []
        for key in ht:
            res.append([key, ht[key]])
        return sorted(res)
