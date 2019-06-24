"""
    1st approach: BFS + memoization
    - BFS
    - to avoid redundant calculation, use (remaining nodes, current node) as key

    Time    O(n2^n)
    Space   O(n2^n)
    732 ms, faster than 6.51%
"""


class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        m = set()
        # put the nodes in the queue
        q = []
        for i in range(len(graph)):
            q.append((i, [i]))
        # BFS
        while len(q) > 0:
            n = len(q)
            for i in range(n):
                node, path = q.pop(0)
                # shortest path must be the first which travelled all the nodes
                if len(set(path)) == len(graph):
                    return len(path)-1
                # explore paths with adjacent nodes
                for child in graph[node]:
                    newPath = path+[child]
                    # use (remaining nodes, current node) as key to avoid redundant calculation
                    key = self.getKey(graph, newPath, child)
                    if key in m:
                        continue
                    m.add(key)
                    # traverse
                    q.append((child, newPath))
        return 0

    def getKey(self, graph, path, idx):
        arr = []
        m = set(path)
        for i in range(len(graph)):
            if i not in m:
                arr.append(i)
        return (tuple(arr), idx)


s = Solution()

a = [[1, 2, 3], [0], [0], [0]]
print(s.shortestPathLength(a))

a = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
print(s.shortestPathLength(a))

a = [[1, 5], [0, 3], [3, 5], [1, 2, 5], [7],
     [0, 7, 6, 2, 3], [5], [5, 4, 8], [7]]
print(s.shortestPathLength(a))

a = [[1,2,3,4,5,6,7,8,9,10,11],[0,2,3,4,5,6,7,8,9,10,11],[0,1,3,4,5,6,7,8,9,10,11],[0,1,2,4,5,6,7,8,9,10,11],[0,1,2,3,5,6,7,8,9,10,11],[0,1,2,3,4,6,7,8,9,10,11],[0,1,2,3,4,5,7,8,9,10,11],[0,1,2,3,4,5,6,8,9,10,11],[0,1,2,3,4,5,6,7,9,10,11],[0,1,2,3,4,5,6,7,8,10,11],[0,1,2,3,4,5,6,7,8,9,11],[0,1,2,3,4,5,6,7,8,9,10]]
print(s.shortestPathLength(a))