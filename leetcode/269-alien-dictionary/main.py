"""
    questions to ask:
    - will there be invalid sequence? yes
    - lowercase only? yes
    - will there be duplicate words? yes

    pretty good explanation:
    - https://leetcode.com/problems/alien-dictionary/discuss/70169/My-Concise-JAVA-solution-based-on-Topological-Sorting
"""

"""
    1st approach: topological ordering in bfs using queue
    1. construct the edges
    2. topo sort

    Time    O(V+E)
    Space   O(V)
    20 ms, faster than 100.00%
"""


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        edges = []
        nodesSet = set()
        # put the characters in order into the edges
        for i in range(len(words)):
            word = words[i]
            edgeFormed = False
            for j in range(len(word)):
                if edgeFormed == False and i > 0 and j < len(words[i-1]) and words[i][j] != words[i-1][j]:
                    # construct graph, [to, from]
                    edges.append([words[i-1][j], words[i][j]])
                    edgeFormed = True
                nodesSet.add(word[j])
        nodes = list(nodesSet)
        result = self.topoSortInBFS(edges, nodes)
        return ''.join(result)

    def topoSortInBFS(self, prerequisites, nodes):
        """
        :type prerequisites: List[List[string]] e.g. [[to1, from1], [to2, from2],...]
        :rtype: List[string]
        """
        indegrees = {}
        for node in nodes:
            indegrees[node] = 0
        # get all the connections/adjacents list
        connections = {}
        for src, dest in prerequisites:
            # construct adjacent list
            if src not in connections:
                connections[src] = [dest]
            else:
                connections[src].append(dest)
            # add indegree for each node
            indegrees[dest] += 1
        # get the nodes with 0 indegree
        queue = []
        for key in indegrees:
            if indegrees[key] == 0:
                queue.append(key)
        # dequeue node from the queue and put it into the result
        res = []
        while len(queue) > 0:
            dq = queue.pop(0)
            res.append(dq)
            if dq in connections:
                children = connections[dq]
                for child in children:
                    indegrees[child] -= 1
                    if indegrees[child] == 0:
                        queue.append(child)
        # return [] if there is a cycle
        for key in indegrees:
            if indegrees[key] > 0:
                return []
        return res


a = [
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt",
]
print(Solution().alienOrder(a))

a = [
    "z",
    "x",
]
print(Solution().alienOrder(a))

a = [
    "z",
    "x",
    "z",
]
print(Solution().alienOrder(a))

a = [
    "z",
    "z",
]
print(Solution().alienOrder(a))

a = [
    "za",
    "zb",
    "ca",
    "cb",
]
print(Solution().alienOrder(a))


print("-----")

"""
    2nd approach: topological ordering in dfs using recursion and stack
    1. construct the edges
    2. topo sort

    Time    O(V+E)
    Space   O(V)
    32 ms, faster than 23.89%
"""


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        edges = []
        nodesSet = set()
        for i in range(len(words)):
            word = words[i]
            edgeFormed = False
            for j in range(len(word)):
                if edgeFormed == False and i > 0 and j < len(words[i-1]) and words[i][j] != words[i-1][j]:
                    # construct graph, [to, from]
                    edges.append([words[i-1][j], words[i][j]])
                    edgeFormed = True
                nodesSet.add(word[j])
        nodes = list(nodesSet)
        result = self.topoSortInDFS(edges, nodes)
        return ''.join(result)

    def topoSortInDFS(self, prerequisites, nodes):
        # prepare a list to save to children for each node
        connections = {}
        for src, dest in prerequisites:
            # construct adjacent list
            if src not in connections:
                connections[src] = [dest]
            else:
                connections[src].append(dest)
        # iterate all the vertices
        seen = {}
        stack = []
        for node in nodes:
            if node in seen:
                if seen[node] == 1:
                    return []
                elif seen[node] == 2:
                    continue
            if self.exploreVertex(connections, node, seen, stack) == False:
                return []
        res = []
        while len(stack) > 0:
            res.append(stack.pop())
        return res

    def exploreVertex(self, connections, curKey, seen, stack):
        seen[curKey] = 1  # visisting
        if curKey in connections:
            children = connections[curKey]
            for child in children:
                if child in seen:
                    if seen[child] == 1:
                        return False
                    elif seen[child] == 2:
                        continue
                if self.exploreVertex(connections, child, seen, stack) == False:
                    return False
        seen[curKey] = 2  # visisted
        stack.append(curKey)
        return True


a = [
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt",
]
print(Solution().alienOrder(a))

a = [
    "z",
    "x",
]
print(Solution().alienOrder(a))

a = [
    "z",
    "x",
    "z",
]
print(Solution().alienOrder(a))

a = [
    "z",
    "z",
]
print(Solution().alienOrder(a))

a = [
    "za",
    "zb",
    "ca",
    "cb",
]
print(Solution().alienOrder(a))
