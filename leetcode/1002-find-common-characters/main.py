import copy

"""
    1st approach: hashtable

    Time    O(m*(n+m)+m)  m: average length of characters, n: length of input array
    Space   O(n)
    68 ms, faster than 41.70%
"""


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if len(A) == 0:
            return []
        # create a global hashtable
        gHt = {}
        for c in A[0]:
            if c not in gHt:
                gHt[c] = 1
            else:
                gHt[c] += 1
        # delete/update the occurence in global hashtable by checking against the hashtable of each vocab
        for i in range(1, len(A)):
            curHt = {}
            for c in A[i]:
                if c not in curHt:
                    curHt[c] = 1
                else:
                    curHt[c] += 1
            clone = copy.deepcopy(gHt)
            for key in clone:
                if key not in curHt:
                    del gHt[key]
                else:
                    gHt[key] = min(gHt[key], curHt[key])
        # construct result
        res = []
        for c in gHt:
            temp = gHt[c] * [c]
            res += temp
        return res


"""
    2nd approach: hashtable

    Time    O(n*(m+26)+26) m: average length of characters, n: length of input array
    Space   O(n)
    52 ms, faster than 65.55%
"""


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if len(A) == 0:
            return []
        # create a global hashtable
        gHt = 26 * [0]
        for c in A[0]:
            gHt[ord(c)-ord('a')] += 1
        # delete/update the occurence in global hashtable by checking against the hashtable of each vocab
        for i in range(1, len(A)):
            curHt = 26 * [0]
            for c in A[i]:
                curHt[ord(c)-ord('a')] += 1
            for i in range(len(gHt)):
                gHt[i] = min(gHt[i], curHt[i])
        # construct result
        res = []
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(gHt)):
            if gHt[i] > 0:
                temp = gHt[i] * [alphabets[i]]
                res += temp
        return res
