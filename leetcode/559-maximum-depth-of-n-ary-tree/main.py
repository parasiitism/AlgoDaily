class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        result = 0
        stack = []
        stack.append((root, 1))
        while len(stack) > 0:
            pop = stack.pop()
            if pop[1] > result:
                result = pop[1]
            for i in range(len(pop[0].children)):
                stack.append((pop[0].children[i], pop[1]+1))
        return result