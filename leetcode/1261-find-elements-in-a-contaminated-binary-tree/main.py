# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.hs = set()
        self.dfs(root, 0)

    def dfs(self, node, x):
        if node == None:
            return
        node.val = x
        self.hs.add(x)
        self.dfs(node.left, 2*x+1)
        self.dfs(node.right, 2*x+2)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return True if target in self.hs else False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
