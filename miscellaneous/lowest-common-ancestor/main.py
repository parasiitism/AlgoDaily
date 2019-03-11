"""
  LCA of a nary-tree
"""


class Employee(object):
    def __init__(self, name):
        self.name = name
        self.subordinates = []


def lowestCommonManager(root, a, b):
    res = dfs(root, a, b)
    if res != None and root.name == res.name:
        return None
    return res


def dfs(node, a, b):
    if node == None or node.name == a.name or node.name == b.name:
        return node
    res = []
    for child in node.subordinates:
        temp = dfs(child, a, b)
        if temp != None:
            res.append(temp)
    if len(res) == 2:
        return node
    elif len(res) == 1:
        return res[0]
    return None


#       a
#    b       c
#  d   e      f
# ghi   j
a = Employee("a")
b = Employee("b")
c = Employee("c")
d = Employee("d")
e = Employee("e")
f = Employee("f")
g = Employee("g")
h = Employee("h")
i = Employee("i")
j = Employee("j")
a.subordinates = [b, c]
b.subordinates = [d, e]
c.subordinates = [f]
d.subordinates = [g, h, i]
e.subordinates = [j]

# h, i
res = lowestCommonManager(a, h, i)
print(res.name)

# h, j
res = lowestCommonManager(a, h, j)
print(res.name)

# h, f
res = lowestCommonManager(a, h, f)
print(res)
