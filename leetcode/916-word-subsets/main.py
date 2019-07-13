from collections import *

"""
    1st approach: brute-force, hashtable

    Time    O(AB)
    Space   O(A+B)
    LTE
"""


class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        BSet = set(B)
        bStructures = {}
        for b in B:
            temp = self.structure(b)
            key = tuple(temp)
            bStructures[key] = temp

        m = {}
        signatures = defaultdict(list)
        for a in A:
            m[a] = True
            temp = self.structure(a)
            signatures[tuple(temp)].append(a)

        for bKey in bStructures:
            bStructure = bStructures[bKey]
            for sign in signatures:
                aStructure = list(sign)
                if self.aHasB(aStructure, bStructure) == False:
                    arr = signatures[sign]
                    for x in arr:
                        m[x] = False

        res = []
        for x in m:
            if m[x] == True:
                res.append(x)
        return res

    def structure(self, s):
        res = 26*[0]
        for c in s:
            idx = ord(c) - ord('a')
            res[idx] += 1
        return res

    def aHasB(self, a, b):
        for i in range(26):
            if b[i] > a[i]:
                return False
        return True


"""
    2nd approach: reduce B to a single word
    - reduce B to a single word
    - see if a contains that single word

    Time    O(A+B)
    Space   O(A+B)
    1180 ms, faster than 64.90%
"""


class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        oneB = 26 * [0]
        for b in B:
            temp = self.structure(b)
            for i in range(26):
                oneB[i] = max(temp[i], oneB[i])

        res = []
        for a in A:
            structureA = self.structure(a)
            if self.aHasB(structureA, oneB):
                res.append(a)

        return res

    def structure(self, s):
        res = 26*[0]
        for c in s:
            idx = ord(c) - ord('a')
            res[idx] += 1
        return res

    def aHasB(self, a, b):
        for i in range(26):
            if b[i] > a[i]:
                return False
        return True
