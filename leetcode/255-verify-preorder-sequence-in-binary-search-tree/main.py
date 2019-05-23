"""
    1st approach: stack, learned from others
    - The idea is to use a stack. This problem is similar to The Next Greater Element
    - Here we find next greater element and after finding next greater, if we find a smaller element, then return false.

    for a node in BST
    1. any node in the left subtree must be less than its value
    2. any node in the right subtree must be larger than its value

    ref:
    - https://www.geeksforgeeks.org/check-if-a-given-array-can-represent-preorder-traversal-of-binary-search-tree/
"""


class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        minNodeVal = -sys.maxsize
        for num in preorder:
            if num < minNodeVal:
                return False
            while len(stack) > 0 and num > stack[-1]:
                minNodeVal = stack.pop()
            stack.append(num)
        return True
