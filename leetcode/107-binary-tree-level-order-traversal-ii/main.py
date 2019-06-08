# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: BFS

    Time    O(n)
    Space   O(h)
    24 ms, faster than 87.85%
"""


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = []
        q = [root]
        while len(q) > 0:
            n = len(q)
            arr = []
            for i in range(n):
                pop = q.pop(0)
                arr.append(pop.val)
                if pop.left != None:
                    q.append(pop.left)
                if pop.right != None:
                    q.append(pop.right)
            res.append(arr)
        return res[::-1]
