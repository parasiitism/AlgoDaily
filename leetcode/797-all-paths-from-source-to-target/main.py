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

        source, target = 0, len(graph)-1
        res = []
        q = []
        q.append((source, [source]))
        while len(q) > 0:
            head, path = q.pop(0)
            if head == target:
                res.append(path)
                continue
            for child in graph[head]:
                q.append((child, path + [child]))
        return res


"""
    2nd approach: DFS
    - since the question mentions that the graph is acyclic, we dont even need to worry if a node will be visited again in a cycle
    - therefore a simple DFS is good

    Time    O(n)
    Space   O(n)
    96 ms, faster than 36.78%
"""


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(0, [0], len(graph)-1, graph)
        return self.res

    def dfs(self, cur, path, target, graph):
        if cur == target:
            self.res.append(path)
            return
        for child in graph[cur]:
            self.dfs(child, path+[child], target, graph)
