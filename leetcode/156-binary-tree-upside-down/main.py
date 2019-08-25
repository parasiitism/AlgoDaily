# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st: preorder traversal + construct a new tree
    - keep in mind of the below cases

    e.g.
            1
          /
        2
      /  
    3

    e.g.
                1
              /
            2
          /   \
        3      5
      /
    4

    Time    O(n)
    Space   O(n)
    12 ms, faster than 94.75%
"""


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.root = None
        self.cur = None
        self.level = -1
        self.postOrder(root, 0)
        return self.root

    def postOrder(self, node, level):
        if node == None:
            return
        self.postOrder(node.left, level+1)
        self.postOrder(node.right, level+1)

        if self.cur == None:
            self.cur = TreeNode(node.val)
            self.root = self.cur
            self.level = level
        else:
            if level != self.level:
                self.cur.right = TreeNode(node.val)
                self.cur = self.cur.right
                self.level = level
            else:
                if self.cur.left == None:
                    self.cur.left = TreeNode(node.val)
                elif self.cur.right == None:
                    self.cur.right = TreeNode(node.val)
                    self.cur = self.cur.right
                    self.level = level - 1


"""
    2nd: BFS + construct
    - keep in mind of the below cases

    e.g.
            1
          /   \
        2       3
      /   \ 
    4       5

    storeys
    [
        [1],
        [2,3],
        [4,5],
    ]
    then build the tree from the array

    Time    O(2n)
    Space   O(n)
    20 ms, faster than 57.27%
"""


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        q = [root]
        arr = []
        while len(q) > 0:
            n = len(q)
            temp = []
            for i in range(n):
                node = q.pop(0)
                temp.append(TreeNode(node.val))
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            arr.append(temp)

        root = None
        cur = None
        while len(arr) > 0:
            temp = arr.pop()
            if root == None:
                root = temp[0]
                cur = root
            cur.val = temp[0].val
            if len(temp) > 1:
                cur.left = temp[1]

            if len(arr) > 0:
                cur.right = TreeNode(-1)
                cur = cur.right
        return root
