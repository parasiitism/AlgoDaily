class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

# recursive
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        for n in root.children:
            ans.extend(self.postorder(n))
        ans.append(root.val)
        return ans

# iterative
class Solution1(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        stack.append(root)
        result = []
        while len(stack) > 0:
            pop = stack.pop()
            result = [pop.val] + result
            # mind the order of the children
            for i in range(len(pop.children)):
                stack.append(pop.children[i])
        return result