# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: bfs + lowest common ancestor
    
    Time    O(kn) -> O(n^2) worst
    Space   O(n)
    16 ms, faster than 33.55%
"""


class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        q = [root]
        leaves = []
        while len(q) > 0:
            n = len(q)
            arr = []
            for i in range(n):
                head = q.pop(0)
                arr.append(head)
                if head.left != None:
                    q.append(head.left)
                if head.right != None:
                    q.append(head.right)
            leaves = arr
        res = leaves[0]
        for i in range(1, len(leaves)):
            res = self.lcs(root, leaves[i], res)
        return res

    def lcs(self, node, p, q):
        if node == None or node == p or node == q:
            return node
        left = self.lcs(node.left, p, q)
        right = self.lcs(node.right, p, q)
        if left != None and right != None:
            return node
        if left != None:
            return left
        return right
