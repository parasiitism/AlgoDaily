"""
    1st approach: hashtable + string
    - if the current index is one of the indexes, slice the S with the length of sources[i]
    - if the slice == sources[i], append targets[i] to the result
    - else return append original character in the result one by one

    Time    O(m+n)
    Space   O(n)
    20 ms, faster than 97.15%
"""


class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        indexMap = {}
        for i in range(len(indexes)):
            indexMap[indexes[i]] = i

        res = ""
        i = 0
        while i < len(S):
            if i in indexMap:
                idx = indexMap[i]
                n = len(sources[idx])
                temp = S[i:i+n]
                if temp == sources[idx]:
                    res += targets[idx]
                    i = i+n
                else:
                    res += S[i]
                    i += 1
            else:
                res += S[i]
                i += 1
        return res
