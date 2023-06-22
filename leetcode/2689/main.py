"""
    DFS

    Time    O(N)
    Space   O(H)
"""

# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        S = ''
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node.len == 0:
                S += node.val
            if len(S) >= k:
                return S[k-1]
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ''
