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
    - ids are numbers, start from 1
    - we are sure that all the edges belong to the same set/cluster
    """
    wareHousesSet = set()
    for edge in edges:
        wareHousesSet.add(edge[0])
        wareHousesSet.add(edge[1])

    wareHouses = list(wareHousesSet)
    # the ids start from 1, i dont want to assign 0->1, 1->2, so i just simply add one dummy cap at index 0
    c = UnionFind(len(wareHouses)+1)

    res = []
    edges = sorted(edges, key=lambda x: x[2])
    for edge in edges:
        c1 = c.find(edge[0])
        c2 = c.find(edge[1])
        if c1 != c2:
            c.union(edge[0], edge[1])
            res.append(edge)
    return res


class UnionFind(object):
    def __init__(self, n):
        self.count = 0
        self.ids = []
        self.caps = []
        for i in range(n):
            self.ids.append(i)
            self.caps.append(1)

    def getCount(self):
        return self.count

    def find(self, key):
        # loop to find to ultimate root
        if key < len(self.ids):
            cur = key
            while cur != self.ids[cur]:
                cur = self.ids[cur]
            return cur
        return -1

    def union(self, p, q):
        if p < 0 or p+1 > len(self.ids) or q < 0 or q+1 > len(self.ids):
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
        if p < 0 or p+1 > len(self.ids) or q < 0 or q+1 > len(self.ids):
            return
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
