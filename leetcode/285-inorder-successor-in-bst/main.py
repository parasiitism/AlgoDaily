# leetcode doesn't support go for this question, i did it in python first

import sys
# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

# my intuitive thought: find the smallest node which is just larger than the target
# O(logn)
class Solution(object):
  dest = None
  found = False

  def inorderSuccessor(self, root, p):
    """
    :type root: TreeNode
    :type p: TreeNode
    :rtype: TreeNode
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
