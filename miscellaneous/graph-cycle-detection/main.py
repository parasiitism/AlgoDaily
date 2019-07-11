"""
    detect if a directed graph has a cycle
"""

"""
    1st approach: DFS + hashtable
    - similar to lc802
    - for each node, dfs to see if that node might reach to a cycle
    - use hashtable to catch the result of the visited nodes.
        - for a new node, we first mark it as unsafe(reach to a cycle), then traverse
        - if we can eventually reach to a terminal(no cycle), backtrack corresponding nodes in that path as safe
        - next time when we visit a visited node, just return if it is safe or unsafe
    
    ref:
    - https://www.geeksforgeeks.org/detect-cycle-in-a-graph/

    Time    O(N+E)
    Space   O(N)
"""


class Solution(object):
    def detectCycle(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        if len(graph) == 0:
            return []
        # 0: unvisited, 1: hascycle, 2: nocycle
        seen = len(graph) * [0]
        res = []
        for i in range(len(graph)):
            b = self.hasNoCycle(graph, i, seen)
            if b == False:
                return True
        return False

    def hasNoCycle(self, graph, idx, seen):
        if seen[idx] != 0:
            return seen[idx] == 2
        seen[idx] = 1
        for child in graph[idx]:
            b = self.hasNoCycle(graph, child, seen)
            if b == False:
                return False
        seen[idx] = 2
        return True


s = Solution()

a = [[1, 2], [2, 3], [5], [0], [5], [], []]
print(s.detectCycle(a))

a = [[1, 2], [2], [0, 3], []]
print(s.detectCycle(a))

a = [[1, 2], [2], [3], []]
print(s.detectCycle(a))

a = [[1, 2], [2], [3], [3]]
print(s.detectCycle(a))

a = [[1, 2], [2], [3], [], [3]]
print(s.detectCycle(a))

print("-----")


class Solution(object):
    def detectCycle(self, graph):
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
        while len(q):
            node = q.pop()
            for parent in parents[node]:
                outdegree[parent] -= 1
                if outdegree[parent] == 0:
                    q.append(parent)
        # if outdegree[i] > 0, there is a cycle
        for i in range(n):
            if outdegree[i] > 0:
                return True
        return False


s = Solution()

a = [[1, 2], [2, 3], [5], [0], [5], [], []]
print(s.detectCycle(a))

a = [[1, 2], [2], [0, 3], []]
print(s.detectCycle(a))

a = [[1, 2], [2], [3], []]
print(s.detectCycle(a))

a = [[1, 2], [2], [3], [3]]
print(s.detectCycle(a))

a = [[1, 2], [2], [3], [], [3]]
print(s.detectCycle(a))
