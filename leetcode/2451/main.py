"""
    hashtable

    Time    O(N)
    Space   O(N)
    84 ms, faster than 33.33% 
"""


class Solution:
    def oddString(self, words: List[str]) -> str:
        ctr = Counter()
        cache = {}
        for w in words:
            n = len(w)
            diffs = []
            for i in range(1, n):
                diff = ord(w[i]) - ord(w[i-1])
                diffs.append(diff)
            key = tuple(diffs)
            ctr[key] += 1
            cache[key] = w
        for key in ctr:
            cnt = ctr[key]
            if cnt == 1:
                return cache[key]
        return ""
