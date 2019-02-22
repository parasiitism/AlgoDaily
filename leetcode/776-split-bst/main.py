# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]

        this question is super hard
        i gave up an read the ans
        - https://leetcode.com/articles/split-bst
        - https://leetcode.com/problems/split-bst/discuss/159985/Python-DFS-tm

        the basic idea is to split the node into 2 subtree
        1. if target < curNode, split left subtree of the curNode, and reassign the curNode's left subtree
        2. else, split the right subtree of the curNode, and reassign the curNode's right subtree

        """
        if root == None:
            return [None, None]
        if V < root.val:
            # go to left and split left subtree
            left, right = self.splitBST(root.left, V)
            root.left = right
            # return the left and new root
            return [left, root]
        else:
            # go to right and split right subtree
            left, right = self.splitBST(root.right, V)
            root.right = left
            # return the left and new root
            return [root, right]


# helper
def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


#       10
#    5     15
#  2  7  12
a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(15)
d = TreeNode(2)
e = TreeNode(7)
f = TreeNode(12)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
ans1, ans2 = Solution().splitBST(a, 5)
inorder(ans1)
print("---")
inorder(ans2)
