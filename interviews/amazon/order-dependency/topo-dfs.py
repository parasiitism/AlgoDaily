"""
    Topological Sorting/Ordering with DFS

    1. create a connections list to save to children for each node
    2. for each node, put the children in the connections
        e.g. [4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]
        children list = [[], [0], [3], [], [3], [2,4,1]]
    3. use a hashtable to store the visited node, 1=visiting, 2=visited
    4. use a stack to store the nodes which no longer has unvisited children
    5. the result is the stack in the reversed order

    Time    O(V+E)
    Space   O(V)
"""


class Order(object):
    def __init__(self, orderId):
        self.orderId = orderId


class Dependency(object):
    # pre, cur are type of 'Order'
    def __init__(self, cur, pre):
        self.cur = cur
        self.pre = pre


def topologicalOrderingDFS(dependencies):
    connections = {}
    nodesSet = set()
    for dep in dependencies:
        preId = dep.pre.orderId
        curId = dep.cur.orderId
        if dep in connections:
            connections[preId].append(curId)
        else:
            connections[preId] = [curId]
        nodesSet.add(preId)
        nodesSet.add(curId)

    seen = {}
    stack = []
    nodes = list(nodesSet)
    for node in nodes:
        if node in seen:
            if seen[node] == 1:
                return []
            elif seen[node] == 2:
                continue
        if exploreVertex(connections, node, seen, stack) == False:
            return []
    res = []
    while len(stack) > 0:
        res.append(stack.pop())
    return res


def exploreVertex(connections, curKey, seen, stack):
    seen[curKey] = 1
    if curKey in connections:
        children = connections[curKey]
        for child in children:
            if child in seen:
                if seen[child] == 1:
                    return False
                elif seen[child] == 2:
                    continue
            if exploreVertex(connections, child, seen, stack) == False:
                return False
    seen[curKey] = 2
    stack.append(curKey)
    return True


# normal 1: https://www.jianshu.com/p/deceb6173865
a = Order('a')
b = Order('b')
c = Order('c')
d = Order('d')
e = Order('e')
f = Order('f')
dependencies = [
    Dependency(a, b),
    Dependency(d, e),
    Dependency(d, c),
    Dependency(c, f),
    Dependency(b, f),
    Dependency(e, f),
    Dependency(e, b),
]
print(topologicalOrderingDFS(dependencies))


# normal 2: https://www.youtube.com/watch?v=ddTC4Zovtbc
a = Order('a')
b = Order('b')
c = Order('c')
d = Order('d')
e = Order('e')
f = Order('f')
g = Order('g')
h = Order('h')
dependencies = [
    Dependency(g, f),
    Dependency(f, d),
    Dependency(d, b),
    Dependency(f, e),
    Dependency(h, e),
    Dependency(e, c),
    Dependency(c, b),
    Dependency(c, a),
]
print(topologicalOrderingDFS(dependencies))


# 2 graphs
a = Order('a')
b = Order('b')
c = Order('c')
d = Order('d')
e = Order('e')
f = Order('f')
g = Order('g')
h = Order('h')
dependencies = [
    Dependency(a, b),
    Dependency(d, e),
    Dependency(d, c),
    Dependency(c, f),
    Dependency(b, f),
    Dependency(e, f),
    Dependency(e, b),
    Dependency(g, h),
]
print(topologicalOrderingDFS(dependencies))

# cyclic
a = Order('a')
b = Order('b')
c = Order('c')
d = Order('d')
e = Order('e')
f = Order('f')
dependencies = [
    Dependency(a, b),
    Dependency(d, e),
    Dependency(d, c),
    Dependency(c, f),
    Dependency(b, f),
    Dependency(e, f),
    Dependency(e, b),
    Dependency(f, d),
]
print(topologicalOrderingDFS(dependencies))
