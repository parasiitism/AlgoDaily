class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

# iterative
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        stack = []
        stack.append(root)
        while len(stack) > 0:
            pop = stack.pop()
            result.append(pop.val)
            # be careful:
            # when we pop the stack, the order of children is reserved,
            # so we need to put the children in the stack in a reserved order
            for i in range(len(pop.children)):
                idx = len(pop.children)-1-i
                stack.append(pop.children[idx])
        return result

# recursive
class Solution(object):
    def preorder(self, root):
          """
          :type root: Node
          :rtype: List[int]
          """
          if not root:
              return []
          ans = []
          ans.append(root.val)
          for n in root.children:
              ans.extend(self.preorder(n))
          return ans