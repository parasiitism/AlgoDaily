# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    iterative dfs
    
    Time    O(n)
    Space   O(h)
"""


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


"""
    2nd approach: recursive dfs

    Time    O(n)
    Space   O(h)
    24 ms, faster than 97.03%
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)

    def dfs(self, node):
        if node == None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        return max(left, right)+1
