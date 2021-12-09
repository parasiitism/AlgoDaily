
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: lowest common ancestor + dfs

    Time    O(N+N)
    Space   O(N)
    TLE ?!?!
"""


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lcaNode = self.lca(root, startValue, destValue)
        startPath = self.dfs(lcaNode, startValue, '')
        destPath = self.dfs(lcaNode, destValue, '')
        return len(startPath) * 'U' + destPath

    def lca(self, node, p, q):
        if node == None or node.val == p or node.val == q:
            return node
        left = self.lca(node.left, p, q)
        right = self.lca(node.right, p, q)
        if left != None and right != None:
            return node
        return left if left != None else right

    def dfs(self, node, x, path):
        if node == None:
            return None
        if node.val == x:
            return path
        left = self.dfs(node.left, x, path + 'L')
        right = self.dfs(node.right, x, path + 'R')
        if left:
            return left
        return right


"""
    2nd: same as 1st optimize the runtime by
    1. using inner function
    2. stack-based DFS

    Time    O(N+N)
    Space   O(N)
    1116 ms, faster than 80.00%
"""


class Solution(object):
    def getDirections(self, root, p, q):

        def lca(node):
            if node == None or node.val == p or node.val == q:
                return node
            left = lca(node.left)
            right = lca(node.right)
            if left and right:
                return node
            return left if left else right
        lcaNode = lca(root)

        def dfs(x):
            stack = [(lcaNode, "")]
            while len(stack) > 0:
                node, path = stack.pop()
                if node.val == x:
                    return path
                if node.left:
                    stack.append((node.left, path + "L"))
                if node.right:
                    stack.append((node.right, path + "R"))

        startPath = dfs(p)
        destPath = dfs(q)

        return len(startPath) * 'U' + destPath
