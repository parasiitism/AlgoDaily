class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  
  # notion: common anestor of 2 nodes must inclusively lies between left and right
  # left <= anestor <= right
  # e.g. 3 < 4 < 5
  def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    curr = root
    left = p if p.val < q.val else q
    right = q if q.val > p.val else p
    while True:
      if curr.left != None and right.val < curr.val:
        curr = curr.left
      elif curr.right != None and left.val > curr.val:
        curr = curr.right
      else:
        return curr

# checkout main_test