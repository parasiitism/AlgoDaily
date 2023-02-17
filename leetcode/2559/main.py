"""
    prefix sum

    Time    O(N)
    Space   O(N)
"""
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        pfs = 0
        pfss = (n+1) * [0]
        for i in range(n):
            w = words[i]
            if w[0] in 'aeiou' and w[-1] in 'aeiou':
                pfs += 1
            pfss[i+1] = pfs
        res = []
        for L, R in queries:
            res.append(pfss[R+1] - pfss[L])
        return res