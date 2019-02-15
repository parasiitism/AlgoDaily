class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]

        1st approach: Union Find
        - implement an Union Find
        - for each edge, union the node if they are not connected
        - but if they both present in the union set, put it into the result

        The purpose of this question is to practice Union Find, I am gonna do it in other ways

        Time    O(nlogn) iterate the edges, in each iteration the Find() operation is O(logn)
        Space   O(n) the set
        28 ms, faster than 69.39% 
        """
        nodesSet = set()
        for edge in edges:
            nodesSet.add(edge[0])
            nodesSet.add(edge[1])
        nodes = list(nodesSet)
        uf = UnionFind(nodes)
        res = None
        for edge in edges:
            temp = uf.union(edge[0], edge[1])
            if temp == False:
                res = edge
        if uf.getCount() > 1:
            return []
        return res


class UnionFind(object):
    def __init__(self, vertices):
        self.count = len(vertices)
        self.ids = {}
        self.caps = {}
        for vertex in vertices:
            self.ids[vertex] = vertex
            self.caps[vertex] = 1

    def getCount(self):
        return self.count

    # loop to find to ultimate root
    def find(self, key):
        cur = key
        while cur != self.ids[cur]:
            cur = self.ids[cur]
        return cur

    # attach to a larger tree
    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return False

        if self.caps[pId] < self.caps[qId]:
            self.ids[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.ids[qId] = pId
            self.caps[pId] += self.caps[qId]
        self.count -= 1
        return True

    def isConnect(self, p, q):
        return self.find(p) == self.find(q)


print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
print(Solution().findRedundantConnection(
    [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
print(Solution().findRedundantConnection(
    [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5], [4, 5]]))
print(Solution().findRedundantConnection(
    [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5], [6, 7]]))
