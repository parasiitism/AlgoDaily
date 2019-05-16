class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [root]
        while q[0] != None:
            node = q.pop(0)
            q.append(node.left)
            q.append(node.right)
        while len(q) > 0 and q[0] == None:
            q.pop(0)
        return len(q) == 0
