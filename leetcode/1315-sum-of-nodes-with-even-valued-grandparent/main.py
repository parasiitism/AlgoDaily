# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: recursive DFS
    
    Time    O(N)
    Space   O(N)
    104 ms, faster than 62.75%
"""


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, None, None)
        return self.res

    def dfs(self, node: TreeNode, parent: TreeNode, grandParent: TreeNode) -> None:
        if node == None:
            return
        if grandParent != None and grandParent.val % 2 == 0:
            self.res += node.val
        self.dfs(node.left, node, parent)
        self.dfs(node.right, node, parent)


"""
    2nd: iteratively BFS
    
    Time    O(N)
    Space   O(N)
    104 ms, faster than 62.75%
"""


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        q = [(root, None, None)]
        while len(q) > 0:
            node, p, gp = q.pop(0)
            if gp != None and gp.val % 2 == 0:
                res += node.val
            if node.left != None:
                q.append((node.left, node, p))
            if node.right != None:
                q.append((node.right, node, p))
        return res
