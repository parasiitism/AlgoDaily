# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: recursive DFS

    Time    O(n)
    Space   O(n)
    84 ms, faster than 62.42%
"""


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
        self.hs.add(x)
        self.dfs(node.left, 2*x+1)
        self.dfs(node.right, 2*x+2)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return True if target in self.hs else False


"""
    2nd: BFS

    Time    O(n)
    Space   O(n)
    68 ms, faster than 99.38%
"""


class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.hs = set()
        self.bfs(root)

    def bfs(self, root):
        q = [(root, 0)]
        while len(q) > 0:
            node, x = q.pop(0)
            self.hs.add(x)
            if node.left != None:
                q.append((node.left, 2*x+1))
            if node.right != None:
                q.append((node.right, 2*x+2))

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return True if target in self.hs else False
