"""
    This is a followup of lc543: Diameter of Binary Tree

    Time    O(N)
    Space   O(h)
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.children = []


class Solution(object):

    def solve(self, root):
        self.result = 0
        self.dfs(root)
        return self.result

    def dfs(self, node):
        max1 = 0
        max2 = 0
        for child in node.children:
            h = self.dfs(child)
            if h > max1:
                max2 = max1
                max1 = h
            elif h > max2:
                max2 = h
        self.result = max(self.result, max1 + max2)
        return max1 + 1


"""
                        a 
                      /   \
                    b       c
                  / | \      | \
                d   e   f    g  h
                i       j
                k       l
                        m
"""

a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')
d = TreeNode('d')
e = TreeNode('e')
f = TreeNode('f')
g = TreeNode('g')
h = TreeNode('h')
i = TreeNode('i')
j = TreeNode('j')
k = TreeNode('k')
l = TreeNode('l')
m = TreeNode('m')

a.children = [b, c]
b.children = [d, e, f]
c.children = [g, h]
d.children = [i]
f.children = [j]
i.children = [k]
j.children = [l]
l.children = [m]


S = Solution()
print(S.solve(a))  # 7: kidbfjlm
