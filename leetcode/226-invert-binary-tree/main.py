# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode

        class approach: recursion

        Time  O(n)
        Space O(h)
        24 ms, faster than 26.24%
        """
        if root == None:
            return None
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode

        class approach: iterative bfs

        Time  O(n)
        Space O(1)
        20 ms, faster than 69.85%
        """
        if root == None:
            return None
        q = []
        q.append(root)
        while len(q) > 0:
            head = q.pop(0)
            temp = head.left
            head.left = head.right
            head.right = temp
            if head.left != None:
                q.append(head.left)
            if head.right != None:
                q.append(head.right)
        return root
