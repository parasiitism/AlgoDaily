from collections import defaultdict

"""
    1st: brute force BFS
    - from 0 to N-1, bfs the the shortest path

    Time    O(N^E)
    Space   O(E)
    224 ms, faster than 5.73%
"""


class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        red = defaultdict(list)
        blue = defaultdict(list)
        for src, dest in red_edges:
            red[src].append([dest, 'red'])
        for src, dest in blue_edges:
            blue[src].append([dest, 'blue'])
        res = [0]
        for i in range(1, n):
            steps = self.bfs(i, red, blue)
            # print('from', i, steps)
            res.append(steps)
        return res

    def bfs(self, target, red, blue):
        q = []
        if 0 in red:
            q += [x+[1] for x in red[0]]
        if 0 in blue:
            q += [x+[1] for x in blue[0]]
        hs = set()
        while len(q) > 0:
            node, color, steps = q.pop(0)
            if (node, color) in hs:
                continue
            hs.add((node, color))
            # print(node, color, steps, target)
            if node == target:
                return steps
            if color == 'blue' and node in red:
                q += [x+[steps+1] for x in red[node]]
            if color == 'red' and node in blue:
                q += [x+[steps+1] for x in blue[node]]
        return -1


s = Solution()

# [0,1,-1]
a = 3
b = [[0, 1], [1, 2]]
c = []
print(s.shortestAlternatingPaths(a, b, c))

# [0,1,-1]
a = 3
b = [[0, 1]]
c = [[2, 1]]
print(s.shortestAlternatingPaths(a, b, c))

# [0,-1,-1]
a = 3
b = [[1, 0]]
c = [[2, 1]]
print(s.shortestAlternatingPaths(a, b, c))

# [0,1,2]
a = 3
b = [[0, 1]]
c = [[1, 2]]
print(s.shortestAlternatingPaths(a, b, c))

# [0,1,1]
a = 3
b = [[0, 1], [0, 2]]
c = [[1, 0]]
print(s.shortestAlternatingPaths(a, b, c))

# [0,1,-1]
a = 3
b = [[0, 1], [2, 0]]
c = [[1, 0]]
print(s.shortestAlternatingPaths(a, b, c))

# [0,1,-1]
a = 5
b = [[1, 2], [3, 1]]
c = [[0, 1], [1, 4], [2, 3]]
print(s.shortestAlternatingPaths(a, b, c))
