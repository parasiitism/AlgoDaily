"""
  amazon oa2
  ref:
  - https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=468231&extra=&page=1
"""


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


"""
in python 2.7, u cant access the outer function. u can just declare in the outer most scope and use global
in python 3.x, u can use nonlocal to access outer function variables
"""

res = 0
target = None


def findMaxAverageSubtree(root):
    def dfs(node):
        global res, target
        if node == None:
            return
        acc = 0
        for child in node.children:
            acc += child.val

        if len(node.children) > 0:
            average = float(acc) / len(node.children)
            if average > res:
                res = average
                target = node

        for child in node.children:
            dfs(child)

    dfs(root)
    return target


#       1
#   2   3   4
# 5   6
a = Node(1, [])
b = Node(2, [])
c = Node(3, [])
d = Node(4, [])
e = Node(5, [])
f = Node(6, [])
a.children = [b, c, d]
b.children = [e, f]

print(findMaxAverageSubtree(a).val)  # 2
