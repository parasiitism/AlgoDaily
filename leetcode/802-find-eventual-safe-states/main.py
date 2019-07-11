"""
    1st approach: dfs(backtracking) + hashset
    - for each node, dfs to see if that node might reach to a cycle
    - use hashtable to catch the visited nodes in each path, backtrack the nodes when we explore somewhere else

    Time    O(N^2) because for each node, its path can only have n-1 distinct nodes
    TLE
"""


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for i in range(len(graph)):
            seen = set()
            b = self.dfs(graph, i, seen)
            if b == True:
                res.append(i)
        return res

    def dfs(self, graph, idx, seen):
        if idx in seen:
            return False
        seen.add(idx)
        for child in graph[idx]:
            # seen.add(child)
            b = self.dfs(graph, child, seen)
            if b == False:
                return False
            seen.remove(child)
        return True


"""
    2nd approach: dfs(backtracking) + hashtable
    - for each node, dfs to see if that node might reach to a cycle
    - use hashtable to catch the result of the visited nodes.
        - for a new node, we first mark it as unsafe(reach to a cycle), then traverse
        - if we can eventually reach to a terminal(no cycle), backtrack corresponding nodes in that path as safe
        - next time when we visit a visited node, just return if it is safe or unsafe

    Time    O(N+E)
    Space   O(N)
    648 ms, faster than 46.53%
"""


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        if len(graph) == 0:
            return []
        seen = len(graph) * [0]  # 0: unvisited, 1: unsafe, 2: safe
        res = []
        for i in range(len(graph)):
            b = self.dfs(graph, i, seen)
            if b == True:
                res.append(i)
        return res

    def dfs(self, graph, idx, seen):
        if seen[idx] != 0:
            return seen[idx] == 2
        seen[idx] = 1
        for child in graph[idx]:
            b = self.dfs(graph, child, seen)
            if b == False:
                return False
        seen[idx] = 2
        return True


s = Solution()

a = [[1, 2], [2, 3], [5], [0], [5], [], []]
print(s.eventualSafeNodes(a))

print("-----")

"""
    3rd approach: bfs(topo sort) + hashtable(out degree)
    - record all the parents&outdegree of each node (topo: children&indegree)
    - we put all the zero-outdegreed nodes into result, imagine that we are peeling off the outer layer of the graph
    - use the fact that if node's outdegree never get down to zero, that node is within a cycle

    Time    O(N+E)
    Space   O(N)
    644 ms, faster than 50.15%
"""


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        if len(graph) == 0:
            return []

        n = len(graph)
        # record all the parents of each node
        parents = {}
        for i in range(n):
            parents[i] = []
        # find the outdegree of each node
        outdegree = n * [0]
        for i in range(n):
            for node in graph[i]:
                parents[node].append(i)
            outdegree[i] = len(graph[i])
        # queue: start from the outer layer(node's outdegree == 0)
        q = []
        for i in range(n):
            if outdegree[i] == 0:
                q.append(i)
        # BFS
        res = []
        while len(q):
            node = q.pop()
            res.append(node)
            for parent in parents[node]:
                outdegree[parent] -= 1
                if outdegree[parent] == 0:
                    q.append(parent)
        return sorted(res)


s = Solution()

a = [[1, 2], [2, 3], [5], [0], [5], [], []]
print(s.eventualSafeNodes(a))
