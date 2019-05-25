# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        res = 0
        q = [(root, 1)]
        while len(q) > 0:
            node, steps = q.pop(0)
            res = max(res, steps)
            if node.left != None:
                q.append((node.left, steps + 1))
            if node.right != None:
                q.append((node.right, steps + 1))
        return res
