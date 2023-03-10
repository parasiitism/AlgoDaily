"""
    hashtable

    Time    O((A+B)logAB)
    Space   O(A+B)
"""
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ht = Counter()
        for key, x in nums1:
            ht[key] += x
        for key, x in nums2:
            ht[key] += x
        res = []
        keys = sorted(ht.keys())
        for k in keys:
            res.append([k, ht[k]])
        return res