# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.result = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]

        1st approach: recursive dfs

        Time  O(n)
        Space O(h)
        24 ms, faster than 76.92%
        """
        self.dfs(root, "")
        return self.result

    def dfs(self, node, path):
        if node == None:
            return
        newPath = path+"->"+str(node.val)
        if node.left == None and node.right == None:
            self.result.append(newPath[2:])
        self.dfs(node.left, newPath)
        self.dfs(node.right, newPath)
