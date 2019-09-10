"""
    1st approach: union find
    - when we union, union 2 trees to the tree that has the smallest key instead of union to a bigger tree
    
    Time O(nlogn)
    Space O(26)
    24 ms, faster than 96.21%
"""


class Solution(object):
    def smallestEquivalentString(self, A, B, S):
        """
        :type A: str
        :type B: str
        :type S: str
        :rtype: str
        """
        uf = UnionFind()
        for i in range(len(A)):
            a = ord(A[i]) - ord('a')
            b = ord(B[i]) - ord('a')
            uf.union(a, b)
        res = ''
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        for x in S:
            c = ord(x) - ord('a')
            smallestCharIdx = uf.find(c)
            res += alphabets[smallestCharIdx]
        return res


class UnionFind(object):
    def __init__(self):
        self.ids = []
        for i in range(26):
            self.ids.append(i)

    def find(self, key):
        # loop to find to ultimate root
        cur = key
        while cur != self.ids[cur]:
            cur = self.ids[cur]
        return cur

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        # attach to the tree that has the smallest key
        if pId < qId:
            self.ids[qId] = pId
        else:
            self.ids[pId] = qId
