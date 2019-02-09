class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool

        1st approach
        - the question states that there will be no duplicate edges and the graph is undirected, 
        the best approach for the question is to use Union Find

        Time    O(nlogn) # in each iteration, union find takes O(logn)
        Space   O(n)
        32ms beats 58.99%
        """
        uf = UnionFind(n)
        for edge in edges:
            aId = uf.find(edge[0])
            bId = uf.find(edge[1])
            if aId != bId:
                uf.union(edge[0], edge[1])
            else:
                return False
        if uf.getCount() == 1:
            return True
        return False


class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.ids = []
        self.caps = []
        for i in range(n):
            self.ids.append(i)
            self.caps.append(1)

    def getCount(self):
        return self.count

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
        # attach to a bigger tree
        if self.caps[pId] < self.caps[qId]:
            self.ids[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.ids[qId] = pId
            self.caps[pId] += self.caps[qId]
        self.count -= 1

    def isConnect(self, p, q):
        return self.find(p) == self.find(q)


# true
e = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(Solution().validTree(5, e))
# false
e = [[0, 1], [0, 2], [0, 3], [1, 4], [5, 6]]
print(Solution().validTree(7, e))
# false
e = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(Solution().validTree(5, e))
# true
e = [[0, 1], [1, 2], [2, 3], [1, 5], [1, 4], [5, 6]]
print(Solution().validTree(7, e))
# false
e = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4], [5, 6]]
print(Solution().validTree(7, e))
