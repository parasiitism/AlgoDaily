# leetcode doesnt support golang submissions


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    # notion: common anestor of 2 nodes must inclusively lies between left and right
    # left <= anestor <= right
    # e.g. 3 < 4 < 5
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        1nd approach: iterative bst dfs

        Time    O(logn)
        Time    O(logn) height of the bst
        68 ms, faster than 99.7%
        """
        parent = root
        while True:
            if p.val < parent.val and q.val < parent.val:
                parent = parent.left
            elif p.val > parent.val and q.val > parent.val:
                parent = parent.right
            else:
                return parent

# checkout main_test


class Solution(object):

    # notion: common anestor of 2 nodes must inclusively lies between left and right
    # left <= anestor <= right
    # e.g. 3 < 4 < 5
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        2nd approach: recursive bst dfs

        Time    O(logn)
        Time    O(logn) height of the bst
        72 ms, faster than 68.62%
        """
        if root == None or root == p or root == q:
            return root
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
