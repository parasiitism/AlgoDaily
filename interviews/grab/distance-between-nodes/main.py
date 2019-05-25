class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: transform it to a graph and bfs/dfs
"""


def distanceBetweenNodes(root, a, b):
    if root == None:
        return -1
    connections = {}

    def dfs(node, parent):
        arr = [parent, None, None]
        if node.left != None:
            arr[1] = node.left.val
            dfs(node.left, node.val)
        if node.right != None:
            arr[2] = node.right.val
            dfs(node.right, node.val)
        connections[node.val] = arr
    dfs(root, None)

    seen = set()
    q = [(a, 0)]
    while len(q) > 0:
        node, steps = q.pop(0)
        if node in seen:
            continue
        seen.add(node)
        if node == b:
            return steps
        if node in connections:
            cands = connections[node]
            for cand in cands:
                q.append((cand, steps + 1))
    return -1


"""
            1
          /   \
        2       3
      /   \       \
    4      5        6
          / \
         7   8
              \
               9
"""
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
i = TreeNode(9)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
h.right = i

# 1
print(distanceBetweenNodes(a, 1, 2))
# 2
print(distanceBetweenNodes(a, 3, 2))
# 2
print(distanceBetweenNodes(a, 1, 4))
# 3
print(distanceBetweenNodes(a, 7, 9))
# 4
print(distanceBetweenNodes(a, 3, 8))

print("-----")

"""
    2nd approach: dfs/bfs
    - find the lowest common ancestor
    - sum up the depths from LCA to a and LCA to b
"""


def distanceBetweenNodes(root, a, b):

    # find lowest common ancestor
    def LCA(node, a, b):
        if node == None or node.val == a or node.val == b:
            return node
        left = LCA(node.left, a, b)
        right = LCA(node.right, a, b)
        if left != None and right != None:
            return node
        return left if left != None else right
    lca = LCA(root, a, b)

    # if no lowest common ancestor
    if lca == None:
        return -1

    # iterative bfs
    # find depth to a and depth to b
    def depthTo(node, target):
        q = [(node, 0)]
        while len(q) > 0:
            pop, steps = q.pop(0)
            if pop.val == target:
                return steps
            if pop.left != None:
                q.append((pop.left, steps + 1))
            if pop.right != None:
                q.append((pop.right, steps + 1))
        return -1

    # recursive dfs
    # def depthTo(node, target):
    #     if node == None:
    #         return -1
    #     if node.val == target:
    #         return 0
    #     x = depthTo(node.left, target)
    #     if x != -1:
    #         return x + 1
    #     y = depthTo(node.right, target)
    #     if y != -1:
    #         return y + 1
    #     return -1

    depthToA = depthTo(lca, a)
    depthToB = depthTo(lca, b)
    return depthToA + depthToB


# 1
print(distanceBetweenNodes(a, 1, 2))
# 2
print(distanceBetweenNodes(a, 3, 2))
# 2
print(distanceBetweenNodes(a, 1, 4))
# 3
print(distanceBetweenNodes(a, 7, 9))
# 4
print(distanceBetweenNodes(a, 3, 8))
