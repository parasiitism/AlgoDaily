class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def topSideView(self, root):
        if root == None:
            return []
        leftArr = []
        rightArr = []
        self.leftdfs(root.left, 0, leftArr)
        self.rightdfs(root.right, 0, rightArr)
        return leftArr[::-1] + [root.val] + rightArr

    def leftdfs(self, node, col, leftArr):
        if node == None:
            return
        if col <= 0 and abs(col) == len(leftArr):
            leftArr.append(node.val)
        self.leftdfs(node.left, col-1, leftArr)
        self.leftdfs(node.right, col+1, leftArr)

    def rightdfs(self, node, col, rightArr):
        if node == None:
            return
        if col == len(rightArr):
            rightArr.append(node.val)
        self.rightdfs(node.left, col-1, rightArr)
        self.rightdfs(node.right, col+1, rightArr)


"""
            1
          /   \
        2       3
          \       \
          4         5
         /
        6
      /
    7
"""
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
a.left = b
a.right = c
b.right = d
c.right = e
d.left = f
f.left = g

print(Solution().topSideView(a))
