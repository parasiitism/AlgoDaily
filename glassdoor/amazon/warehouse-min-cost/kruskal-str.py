def warehouseMinCost(edges):
    """
    Your are given a list of routes, <warehouseA, warehouseB, cost>, 
    write a function to return a collections which go through all the warehouses with minimum cost.

    Idea: Kruskal

    input:
    - edges: an array of edges, (warehouse1, warehouse2, cost)

    return:
    - a colletion of edges which connect all the warehouses

    Cautions
    - u r given all the edges
    - ids are strings
    """
    wareHousesSet = set()
    for edge in edges:
        wareHousesSet.add(edge[0])
        wareHousesSet.add(edge[1])

    wareHouses = list(wareHousesSet)
    c = UnionFind(wareHouses)

    res = []
    # or we can use heap
    edges = sorted(edges, key=lambda x: x[2])
    for edge in edges:
        c1 = c.find(edge[0])
        c2 = c.find(edge[1])
        if c1 != c2:
            c.union(edge[0], edge[1])
            res.append(edge)
    # if number of clusters > 1, it means we cannot connect all the nodes no matter how
    if c.getCount() > 1:
        return []
    return res


class UnionFind(object):
    def __init__(self, vertices):
        self.count = len(vertices)
        self.ids = {}
        self.caps = {}
        for vertex in vertices:
            self.ids[vertex] = vertex
            self.caps[vertex] = 1

    def getCount(self):
        return self.count

    def find(self, key):
        # loop to find to ultimate root
        if key not in self.ids:
            return None
        cur = key
        while cur != self.ids[cur]:
            cur = self.ids[cur]
        return cur

    def union(self, p, q):
        if p not in self.ids or q not in self.ids:
            return

        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return

        if self.caps[pId] < self.caps[qId]:
            self.ids[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.ids[qId] = pId
            self.caps[pId] += self.caps[qId]
        self.count -= 1

    def isConnect(self, p, q):
        if p not in self.ids or q not in self.ids:
            return None
        return self.find(p) == self.find(q)


a = [(1, 2, 4),
     (1, 6, 2),
     (2, 6, 5),
     (2, 3, 6),
     (3, 6, 1),
     (4, 5, 2),
     (5, 6, 4),
     (3, 4, 3)]

print(warehouseMinCost(a))

a = [
    ('a', 'b', 4),
    ('a', 'f', 2),
    ('b', 'f', 5),
    ('b', 'c', 6),
    ('c', 'f', 1),
    ('d', 'e', 2),
    ('e', 'f', 4),
    ('c', 'd', 3)
]

print(warehouseMinCost(a))

a = [
    ('a', 'b', 4),
    ('a', 'f', 2),
    ('b', 'f', 5),
    ('b', 'c', 6),
    ('c', 'f', 1),
    ('d', 'e', 2),
    ('e', 'f', 4),
    ('c', 'd', 3),
    ('g', 'h', 1),
]

print(warehouseMinCost(a))
