import bisect

"""
    1st: hashtable + binary search

    Time    O(Q + W + QlognW)
    Space   O(Q + W)
    84 ms, faster than 58.23%
"""


class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        a = self.findFrequencyOfSmallestCharacter(queries)
        b = self.findFrequencyOfSmallestCharacter(words)
        b = sorted(b)

        res = []
        for x in a:
            idx = bisect.bisect_right(b, x)
            res.append(len(b) - idx)
        return res

    def findFrequencyOfSmallestCharacter(self, words):
        ht = []
        for _ in words:
            ht.append(26 * [0])
        arr = []
        for i in range(len(words)):
            w = words[i]
            sIdx = 26
            res = 0
            for c in w:
                idx = ord(c) - ord('a')
                ht[i][idx] += 1
                if idx <= sIdx:
                    res = ht[i][idx]
                    sIdx = idx
            arr.append(res)
        return arr
