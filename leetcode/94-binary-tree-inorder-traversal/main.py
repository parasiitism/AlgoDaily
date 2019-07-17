# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    recursive dfs inorder

    Time    O(n)
    Space   O(h)
"""


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.inorder(root)
        return self.res

    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        self.res.append(node.val)
        self.inorder(node.right)


"""
    iterative dfs inorder

    Time    O(n)
    Space   O(h)
    16 ms, faster than 81.24%
"""


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        cur = root
        while cur != None or len(stack) > 0:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            pop = stack.pop()
            res.append(pop.val)
            cur = pop.right
        return res
