"""
    1st approach: dfs + hashset
    - dfs from source to leafs and check if each leaf is our destination
    - use a hashset to detect cycles

    tricky corner test:
    n = 1
    edges = []
    source = 0
    destination = 0
    should return True

    Time    O(E+V)
    Space   O(n)
    256 ms, faster than 61.16%
"""


class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        # corner case when source == destination and no edges
        if source == destination and len(edges) == 0:
            return True
        # record the adjacent nodes for each node
        connections = []
        for i in range(n):
            connections.append([])
        for src, desc in edges:
            connections[src].append(desc)
        # when destination has adjacent nodes, it must fail
        if len(connections[destination]) > 0:
            return False
        # for each adjacent nodes from source, dfs
        count = 0
        for child in connections[source]:
            # cache visited nodes for cycle detection
            hs = set()
            stack = [child]
            # dfs
            while len(stack) > 0:
                pop = stack.pop()
                # cycle detection
                if pop != destination and pop in hs:
                    return False
                hs.add(pop)
                # when we reach to a leaf, see if it is our destination
                if len(connections[pop]) == 0:
                    if pop == destination:
                        count += 1
                    else:
                        return False
                # traverse
                for node in connections[pop]:
                    stack.append(node)
        return count > 0


s = Solution()

# false
a = 3
b = [[0, 1], [0, 2]]
c = 0
d = 2
print(s.leadsToDestination(a, b, c, d))

# true
a = 4
b = [[0, 1], [0, 2], [1, 3], [2, 3]]
c = 0
d = 3
print(s.leadsToDestination(a, b, c, d))

# true
a = 4
b = [[0, 1], [0, 2], [1, 3], [2, 3], [1, 2]]
c = 0
d = 3
print(s.leadsToDestination(a, b, c, d))

# true
a = 4
b = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 1]]
c = 0
d = 3
print(s.leadsToDestination(a, b, c, d))

# false
a = 4
b = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 1], [1, 2]]
c = 0
d = 3
print(s.leadsToDestination(a, b, c, d))

# false
a = 4
b = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 0]]
c = 0
d = 3
print(s.leadsToDestination(a, b, c, d))

# false
a = 4
b = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 3]]
c = 0
d = 3
print(s.leadsToDestination(a, b, c, d))

# false
a = 3
b = [[0, 1], [1, 1], [1, 2]]
c = 0
d = 2
print(s.leadsToDestination(a, b, c, d))

# false
a = 3
b = [[0, 1], [1, 0], [1, 2]]
c = 0
d = 2
print(s.leadsToDestination(a, b, c, d))

# false
a = 4
b = [[0, 1], [0, 3], [1, 2], [2, 1]]
c = 0
d = 3
print(s.leadsToDestination(a, b, c, d))

# super tricky corner test: true
a = 1
b = []
c = 0
d = 0
print(s.leadsToDestination(a, b, c, d))

# false
a = 1
b = [[0, 0]]
c = 0
d = 0
print(s.leadsToDestination(a, b, c, d))

# false
a = 2
b = [[0, 1], [1, 0]]
c = 0
d = 0
print(s.leadsToDestination(a, b, c, d))
