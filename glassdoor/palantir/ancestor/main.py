from collections import *
"""
    1st:
    Given some edges e.g. [u, v] where u represent the parent and v represent the child, return the nodes who have 0 or 1 parent

    e.g. [
        [1,4],[1,5],[2,5],[3,6],[6,7]
    ]

      1    2    3
    /  \  /      \
    4    5        6
                   \
                    7
"""
def f1(edges):
    nodes = set()
    for u, v in edges:
        nodes.add(u)
        nodes.add(v)
    indegrees = { x: set() for x in nodes }
    for u, v in edges:
        indegrees[v].add(u)
    res = []
    for node in indegrees:
        parents = indegrees[node]
        if len(parents) <= 1:
            res.append(node)
    return res

a = [[1,4],[1,5],[2,5],[3,6],[6,7]]
print(f1(a))

"""
    2nd:
    With the setting in 1st, write a function to check if 2 nodes have the same common ancester

    e.g.[
        [1,4],[1,5],[2,5],[3,6],[6,7]
    ]
      1    2    3
    /  \  /      \
    4    5        6
                   \
                    7
    
    If node1 = 4, node2 = 5, return True
    If node1 = 4, node2 = 7, return False

    To ask: will there be a cycle? 
"""
def f2(edges, node1, node2):

    nodes = set()
    for u, v in edges:
        nodes.add(u)
        nodes.add(v)
    indegrees = { x: set() for x in nodes }
    for u, v in edges:
        indegrees[v].add(u)

    path1set = set()
    q = [node1]
    while len(q) > 0:
        x = q.pop(0)
        if x in path1set:
            continue
        path1set.add(x)
        for parent in indegrees[x]:
            q.append(parent)
    
    q = [node2]
    while len(q) > 0:
        x = q.pop(0)
        if x in path1set:
            return True
        for parent in indegrees[x]:
            q.append(parent)

    return False

print('-----2-----')

a = [[1,4],[1,5],[2,5],[3,6],[6,7]]
print(f2(a, 4, 5))
print(f2(a, 4, 7))

"""
    3rd: Find the oldest parent i.e. farthest common ancestor

    e.g. [
        [1,4],[1,5],[2,5],[3,6],[6,7],[0,2],[0,3],[-1,0],[-2,-1],[-3,-1],[-4,-3]
    ]               
                -4
                /
       -2     -3
         \   /
          -1
            \
              0
             / \
      1    2    3
    /  \  /      \
    4    5        6
                   \
                    7
    
    If node1 = 5, node2 = 7, return -4 (instead of 0) 
"""
def f3(edges, node1, node2):

    nodes = set()
    for u, v in edges:
        nodes.add(u)
        nodes.add(v)
    indegrees = { x: set() for x in nodes }
    for u, v in edges:
        indegrees[v].add(u)
    
    path1steps = Counter()
    q = [(node1, 0)]
    while len(q) > 0:
        x, steps = q.pop(0)
        if x in path1steps:
            continue
        path1steps[x] = steps
        for parent in indegrees[x]:
            q.append((parent, steps+1))
    
    q = [(node2, 0)]
    res_steps = 0
    res = None
    while len(q) > 0:
        x, steps = q.pop(0)
        if x in path1steps:
            if steps + path1steps[x] > res_steps:
                res_steps = steps + path1steps[x]
                res = x
        for parent in indegrees[x]:
            q.append((parent, steps+1))

    return res

print('-----3-----')
a = [
    [1,4],[1,5],[2,5],[3,6],[6,7],[0,2],[0,3],[-1,0],[-2,-1],[-3,-1],[-4,-3]
]
print(f3(a, 5, 7))
print(f3(a, 4, 7))