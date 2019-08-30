from collections import *

"""
    1st approach: BFS on each node

    Time    O(n^2)
    Space   O(e+n)
    LTE
"""


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        connections = {}
        for i in range(n):
            connections[i] = []
        for s, d in edges:
            connections[s].append(d)
            connections[d].append(s)
        minSteps = -1
        res = []
        for i in range(n):
            width = self.bfs(i, connections)
            if minSteps == -1:
                minSteps = width
                res.append(i)
            elif width < minSteps:
                minSteps = width
                res = [i]
            elif width == minSteps:
                res.append(i)
        return res

    def bfs(self, start, connections):
        ht = {}
        q = [(start, 0)]
        while len(q) > 0:
            head, steps = q.pop(0)
            if head in ht:
                continue
            ht[head] = steps
            children = connections[head]
            for child in children:
                q.append((child, steps+1))
        maxSteps = 0
        for key in ht:
            maxSteps = max(maxSteps, ht[key])
        return maxSteps


"""
    2nd: topological ordering
    - i read the hints from "discuss" talking about topological ordering
    - the basic idea is record the "indegree" of each nodes
        - peel the leaves layer by layer (remove the nodes which indegree == 1)
        - until we reach to a point that there are x <= 2 nodes remain unvisited
        - becos a graph can only have 2 minimum-height-tree roots at most 

    ref:
    - https://leetcode.com/problems/minimum-height-trees/discuss/76149/Share-my-Accepted-BFS-Python-Code-with-O(n)-Time

    Time    O(n)
    Space   O(n)
    240 ms, faster than 38.56%
"""


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        neighbors = defaultdict(list)
        degrees = defaultdict(int)

        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        # put all the leaves into a queue
        q = []
        for i in range(n):
            if degrees[i] == 1:
                q.append(i)

        # a graph can only have 2 minimum-height-tree roots at most
        unvisited = set(range(n))  # put [0,1,2,,...] to the hashset
        while len(unvisited) > 2:
            thisLevel = []
            for u in q:
                unvisited.remove(u)
                for v in neighbors[u]:
                    if v not in unvisited:
                        continue
                    degrees[v] -= 1
                    if degrees[v] == 1:
                        thisLevel.append(v)
            # peel the leaves
            q = thisLevel

        return q
