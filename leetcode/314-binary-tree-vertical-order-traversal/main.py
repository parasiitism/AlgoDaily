# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.max = 0
        self.min = 0

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        1st approach
        1. find the width of the binary tree by dfs
        2. bfs the tree with a corresponding 'diff'
        3. put the node.val into a right subarray of result corresponding to the 'diff'

        Time    O(n)
        Space   O(h+n) the height of tree(recursion) + the result
        24ms beats 100%
        """
        if root == None:
            return []
        self.findWidth(root, 0)
        n = self.max-self.min+1

        res = []
        for i in range(n):
            res.append([])

        q = [(root, 0)]
        while len(q) > 0:
            node, col = q.pop(0)
            res[col-self.min].append(node.val)
            if node.left != None:
                q.append((node.left, col-1))
            if node.right != None:
                q.append((node.right, col+1))

        return res

    def findWidth(self, node, at):
        if node == None:
            return
        self.min = min(self.min, at)
        self.max = max(self.max, at)
        self.findWidth(node.left, at-1)
        self.findWidth(node.right, at+1)


#      1
#    2   3
#  5  6    7
#      8
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
a.left = b
a.right = c
b.left = e
b.right = f
c.right = g
f.right = h
print(Solution().verticalOrder(a))

print(Solution().verticalOrder(None))
