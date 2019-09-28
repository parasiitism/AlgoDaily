"""
    1st: hashtable, very common hashing technique for interviews
    - encode a word to avoid checking the permutation

    e.g. 
    - word in wordlist: yellow to y*ll*w
    - query in queries: yullow to y*ll*w

    Time    O(n)
    Space   O(n)
    192 ms, faster than 63.78%
"""


class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        hs = set(wordlist)
        ht_c = {}
        ht_v = {}
        for w in wordlist:
            key1 = w.lower()
            key2 = "".join("*" if c in "aeiou" else c for c in key1)
            if key1 not in ht_c:
                ht_c[key1] = w
            if key2 not in ht_v:
                ht_v[key2] = w

        res = []
        for q in queries:
            if q in hs:
                res.append(q)
            elif q.lower() in ht_c:
                res.append(ht_c[q.lower()])
            else:
                key = "".join("*" if c in "aeiou" else c for c in q.lower())
                if key in ht_v:
                    res.append(ht_v[key])
                else:
                    res.append("")
        return res
