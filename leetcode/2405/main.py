"""
    2 pointers + hashtable
    Time    O(N)
    Space   O(N)
    516 ms, faster than 28.57%
"""


class Solution:
    def partitionString(self, s: str) -> int:
        n = len(s)
        res = []
        j = 0
        ht = defaultdict(int)
        for i in range(n):
            c = s[i]
            ht[c] += 1
            if ht[c] > 1:
                sub = s[j:i]
                res.append(sub)
                for _c in sub:
                    ht[_c] -= 1
                j = i
        sub = s[j:n]
        res.append(sub)
        return len(res)
