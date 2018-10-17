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

