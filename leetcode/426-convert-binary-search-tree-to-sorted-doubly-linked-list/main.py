"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""

"""
    1st approach: straight forward intuition
    - put the nodes in an array in ascending order
    - update the values of the nodes

    Time    O(2n)
    Space   O(n)
    824 ms, faster than 41.54%
"""


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return None
        nodes = []
        # inorder traversal of a BST is actually a sorted list

        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        inorder(root)
        # dump node for referening
        dump = Node(0, None, nodes[0])
        # iterate the sorted list and update the left and right
        for i in range(len(nodes)):
            left = None
            right = None
            if i == 0:
                left = nodes[-1]
            else:
                left = nodes[i-1]
            if i+1 == len(nodes):
                right = nodes[0]
            else:
                right = nodes[i+1]
            nodes[i].left = left
            nodes[i].right = right

        return dump.right
