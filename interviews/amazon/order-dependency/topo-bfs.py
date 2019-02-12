"""
    Topological Sorting/Ordering with BFS

    1. create a list to save to children for each node
    2. for each node, put the children in
        e.g. [4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]
        children list = [[], [0], [3], [], [3], [2,4,1]]
    3. count the indegree for each node(indegree = the number of incoming edges)
    4. put the nodes with 0 indegree into a queue
    5. if the queue is not empty, append the dequeued node to the result and in the same time decrement it's children's indegree
    6  after decrement, if there are nodes which has 0 indegree, put them into the queue
    7. do 6) and 7) until the queue becomes empty
    8. need a 'cnt' to check if there is a cycle(for detail: see comment)

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


def topologicalOrderingBFS(dependencies):
    connections = {}
    indegrees = {}
    nodesSet = set()
    # get all the nodes
    for dep in dependencies:
        preId = dep.pre.orderId
        curId = dep.cur.orderId
        nodesSet.add(preId)
        nodesSet.add(curId)
    # declare indegree for each node
    nodes = list(nodesSet)
    for node in nodes:
        indegrees[node] = 0
    # connections: adjacents list for each node
    for dep in dependencies:
        preId = dep.pre.orderId
        curId = dep.cur.orderId
        if preId in connections:
            connections[preId].append(curId)
        else:
            connections[preId] = [curId]
        # since curId has 1 incomming edge, it's indegree+1
        indegrees[curId] += 1
    # add zero-indegreed node into the queue
    queue = []
    for node in nodes:
        if indegrees[node] == 0:
            queue.append(node)
    # dequeue node from the queue and put it into the result
    # for all of its children(adajacent vertices), subtract 1 indegree and put the vertices which indegree is 0
    # do until the node becomes empty
    res = []
    # if there is a cycle, some node's indegree never becomes 0 therefore it will never be enqueued
    # hence the count will not be consistent with the number of nodes
    cnt = 0
    while len(queue) > 0:
        head = queue.pop(0)
        res.append(head)
        cnt += 1
        if head in connections:
            children = connections[head]
            for child in children:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)

    if cnt == len(nodes):
        return res
    return []


# normal 1: https://www.jianshu.com/p/deceb6173865 0->5 => f->a
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
print(topologicalOrderingBFS(dependencies))

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
print(topologicalOrderingBFS(dependencies))

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
print(topologicalOrderingBFS(dependencies))

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
print(topologicalOrderingBFS(dependencies))
