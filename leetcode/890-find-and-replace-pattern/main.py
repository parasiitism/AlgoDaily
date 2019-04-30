"""
    1st approach: hashtable
    - check if each word isIsomorphic with the pattern

    Time    O(nk) k: number of characters of pattern
    Space   O(2k)
    24 ms, faster than 70.60%
"""


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for word in words:
            if self.isIsomorphic(word, pattern):
                res.append(word)
        return res

    def isIsomorphic(self, a, b):
        if len(a) != len(b):
            return False
        # forwad and backward
        ht_f = {}
        ht_b = {}
        for i in range(len(a)):
            c1 = a[i]
            c2 = b[i]
            if c1 in ht_f:
                if ht_f[c1] != c2:
                    return False
            if c2 in ht_b:
                if ht_b[c2] != c1:
                    return False
            else:
                ht_f[c1] = c2
                ht_b[c2] = c1
        return True
