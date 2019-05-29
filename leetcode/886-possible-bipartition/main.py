"""
    1st approach: BFS + nodes coloring

    idea learned from others:
    - https://www.youtube.com/watch?v=VlZiMD7Iby4

    Time    O(V+E)
    Space   O(V+E)
    780 ms, faster than 28.52%
"""


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        connections = []
        for _ in range(N+1):
            connections.append([])

        for a, b in dislikes:
            connections[a].append(b)
            connections[b].append(a)

        seen = {}
        for i in range(len(connections)):
            if i not in seen:
                if self.check(connections, i, seen) == False:
                    return False
        return True

    def check(self, connections, start, seen):
        q = [(start, 1)]
        while len(q) > 0:
            pop, color = q.pop(0)
            if pop in seen:
                if seen[pop] != color:
                    return False
                continue
            seen[pop] = color
            vertices = connections[pop]
            for v in vertices:
                q.append((v, -color))
        return True


"""
    2nd approach: recursive DFS + nodes coloring

    idea learned from others:
    - https://www.youtube.com/watch?v=VlZiMD7Iby4

    Time    O(V+E)
    Space   O(V+E)
    660 ms, faster than 53.79%
"""


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        connections = []
        for _ in range(N+1):
            connections.append([])

        for a, b in dislikes:
            connections[a].append(b)
            connections[b].append(a)

        seen = {}
        for i in range(len(connections)):
            if i not in seen:
                if self.check(connections, i, 1, seen) == False:
                    return False
        return True

    def check(self, connections, node, color, seen):
        if node in seen:
            if seen[node] != color:
                return False
            return True
        seen[node] = color
        vertices = connections[node]
        for v in vertices:
            if self.check(connections, v, -color, seen) == False:
                return False
        return True
