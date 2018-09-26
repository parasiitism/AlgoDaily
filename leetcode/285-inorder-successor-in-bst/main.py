# once i have finished, 
# i just realized that leetcode only supports up to python2.7 for this question LOL

import sys
# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

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
    x = root.val - p
    y = sys.maxsize
    
    if self.dest != None:
      y = self.dest.val - p

    if x == 0:
      self.found = True

    if x < y and x > 0:
      self.dest = root
    
    if root.val <= p and root.right != None:
      self.check(root.right, p)
    if root.val > p and root.left != None:
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
ans = Solution().inorderSuccessor(a, 0)
print("ans=", ans)
if ans != None:
  print("ans.val=", ans.val)
