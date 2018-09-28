class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class BSTIterator(object):
  
  def __init__(self, root):
    """
    :type root: TreeNode
    """
    self.arr = []
    self.unfold(root)
      
  def unfold(self, node):
    if node is not None:
      self.unfold(node.left)
      self.arr.append(node)
      self.unfold(node.right)

  def hasNext(self):
    """
    :rtype: bool
    """
    return len(self.arr) > 0

  def next(self):
    """
    :rtype: int
    """
    result = None
    if len(self.arr) > 0:
        result = self.arr[0]
        self.arr = self.arr[1:]
    return result.val

# a = TreeNode(5)
# b = TreeNode(3)
# c = TreeNode(6)
# d = TreeNode(2)
# e = TreeNode(4)
# f = TreeNode(1)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# d.left = f

a = TreeNode(1)
b = TreeNode(2)
b.left = None
a.right = b

i, v = BSTIterator(a), []
while i.hasNext():
  v.append(i.next())

print(v)