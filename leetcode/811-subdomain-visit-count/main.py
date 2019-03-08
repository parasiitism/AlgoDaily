"""
    1. split the string by space
    2. split the domain by .
    3. upsert the cnt to the list of top domains

    Time    O(n)
    Space   O(n)
    48 ms, faster than 99.74%
"""


class Solution(object):
    def subdomainVisits(self, cpdomains):
        ht = {}
        for cpdomain in cpdomains:
            rawCnt, dm = cpdomain.split()
            cnt = int(rawCnt)
            arr = dm.split(".")
            if len(arr) == 2:
                self.upsert(ht, arr[1], cnt)
                self.upsert(ht, dm, cnt)
            elif len(arr) == 3:
                self.upsert(ht, arr[2], cnt)
                self.upsert(ht, arr[1]+"."+arr[2], cnt)
                self.upsert(ht, dm, cnt)
        res = []
        for key in ht:
            temp = str(ht[key])+" "+key
            res.append(temp)
        return res

    def upsert(self, ht, key, val):
        if key not in ht:
            ht[key] = val
        else:
            ht[key] += val
