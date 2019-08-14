"""
    1st approach: BFS
    - since the question mentions that the graph is acyclic, we dont even need to worry if a node will be visited again in a cycle
    - therefore a simple BFS is good

    Time    O(n)
    Space   O(n)
    92 ms, faster than 52.48%
"""


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.res = []
        self.bfs(0, len(graph)-1, graph)
        return self.res

    def bfs(self, source, target, graph):
        q = []
        q.append((source, [0]))
        while len(q) > 0:
            head, path = q.pop(0)
            if head == target:
                self.res.append(path)
                continue
            for child in graph[head]:
                q.append((child, path + [child]))
