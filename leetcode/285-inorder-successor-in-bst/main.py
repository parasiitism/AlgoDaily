# leetcode doesn't support go for this question, i did it in python first

import sys
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    dest = None
    found = False

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode

        1st, my intuitive thought:
        - find the smallest node which is just larger than the target

        Time    O(logn)
        Space   O(h)
        """
        if root == None:
            return None
        self.check(root, p)
        return self.dest if self.found else None

    def check(self, root, p):
        x = root.val - p.val
        y = sys.maxsize

        if self.dest != None:
            y = self.dest.val - p.val

        if x == 0:
            self.found = True

        if x < y and x > 0:
            self.dest = root

        if root.val <= p.val and root.right != None:
            self.check(root.right, p)
        if root.val > p.val and root.left != None:
            self.check(root.left, p)


a = TreeNode(5)
b = TreeNode(3)
c = TreeNode(6)
d = TreeNode(2)
e = TreeNode(4)
f = TreeNode(1)
a.left = b
a.right = c
b.left = d
b.right = e
d.left = f

# try to search every number
ans = Solution().inorderSuccessor(a, e)
print("ans=", ans)
if ans != None:
    print("ans.val=", ans.val)


class Solution(object):
    def __init__(self):
        self.res = None
        self.next = False

    def inorderSuccessor(self, root, p):
        """
        2nd approach:
        - the result, successor, is actually the next item in inorder traversal

        Time    O(n)
        Space   O(h)
        92 ms, faster than 14.18%
        """
        self.dfs(root, p)
        return self.res

    def dfs(self, node, target):
        if node == None:
            return
        self.dfs(node.left, target)
        if self.next == True:
            self.res = node
            self.next = False
        if target == node:
            self.next = True
        self.dfs(node.right, target)


a = TreeNode(5)
b = TreeNode(3)
c = TreeNode(6)
d = TreeNode(2)
e = TreeNode(4)
f = TreeNode(1)
a.left = b
a.right = c
b.left = d
b.right = e
d.left = f

# try to search every number
ans = Solution().inorderSuccessor(a, e)
print("ans=", ans)
if ans != None:
    print("ans.val=", ans.val)


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        3rd: very similar to upper bound binary search BUT
        - here is BSTsearch, only record the sucessor when we go left
        - then the sucessor is either your parent OR your left most leaf in right subtree

        see ./idea.jpeg

        Time    O(logn)
        Space   O(h)
        68 ms, faster than 61.86%
        24apr2019
        """
        node = root
        suc = None
        while node != None:
            if p.val >= node.val:
                node = node.right
            else:
                suc = node
                node = node.left
        return suc


a = TreeNode(5)
b = TreeNode(3)
c = TreeNode(6)
d = TreeNode(2)
e = TreeNode(4)
f = TreeNode(1)
a.left = b
a.right = c
b.left = d
b.right = e
d.left = f

# try to search every number
ans = Solution().inorderSuccessor(a, e)
print("ans=", ans)
if ans != None:
    print("ans.val=", ans.val)


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        4th, decent recursive approach:

        Time    O(logn)
        Space   O(h)
        64 ms, faster than 85.19% 
        21feb2019
        """
        if root == None:
            return None
        if p.val < root.val:
            """
            the below line equals to
            ------
            while node.left != None:
                node = node.left
            """
            left = self.inorderSuccessor(root.left, p)
            if left != None:
                return left
            return root
        else:
            return self.inorderSuccessor(root.right, p)


a = TreeNode(5)
b = TreeNode(3)
c = TreeNode(6)
d = TreeNode(2)
e = TreeNode(4)
f = TreeNode(1)
a.left = b
a.right = c
b.left = d
b.right = e
d.left = f

# try to search every number
ans = Solution().inorderSuccessor(a, e)
print("ans=", ans)
if ans != None:
    print("ans.val=", ans.val)
