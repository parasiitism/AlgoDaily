# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
    1st approach: postorder recursion + hashset
    - we can do postorder traversal and start to delete nodes from the bottom to the top
    - whenever we meet a target, we put the children into result and return None to update the current tree
    - use hashtable to optimize the speed we find the nodes in to_delete

    Time    O(n)
    Space   O(n)
    48 ms, faster than 82.38%
"""


class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        self.res = []
        targets = set(to_delete)
        node = self.deleteNode(root, targets)
        if node != None:
            self.res.append(node)
        return self.res

    def deleteNode(self, node, targets):
        if node == None:
            return None
        node.left = self.deleteNode(node.left, targets)
        node.right = self.deleteNode(node.right, targets)
        if node.val in targets:
            if node.left != None:
                self.res.append(node.left)
            if node.right != None:
                self.res.append(node.right)
            return None
        return node
