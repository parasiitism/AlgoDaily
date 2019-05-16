# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isFullTree(root):
    if root == None:
        return True
    stack = []
    for len(stack) > 0:
        pop = stack.pop()
        if pop.left != None and pop.right != None:
            stack.append(pop.left)
            stack.append(pop.right)
        elif pop.left != None or pop.right != None:
            pass
        else:
            return False
    return True
