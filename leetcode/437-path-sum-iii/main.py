# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: recursive dfs with prefix sum
    
    Time    O(n*h) h: average height of the tree
    Space   O(h)
    408 ms, faster than 55.24%
    1apr2019
"""


class Solution(object):

    def __init__(self):
        self.count = 0

    def pathSum(self, root, target):
        self.helper(root, [], target)
        return self.count

    def helper(self, node, prefixArr, target):
        if node == None:
            return
        newArr = []
        # add up the current value to the items in the prefix sum array
        for s in prefixArr:
            temp = s + node.val
            newArr.append(temp)
            if temp == target:
                self.count += 1
        # add the current value into the prefix sum array
        newArr.append(node.val)
        if node.val == target:
            self.count += 1
        # traverse the children
        self.helper(node.left, newArr, target)
        self.helper(node.right, newArr, target)


"""
    2nd approach: iterative dfs with prefix sum
    
    Time    O(n*h) h: average height of the tree
    Space   O(h)
    336 ms, faster than 58.38%
    1apr2019
"""


class StackItem(object):
    def __init__(self, node, prefixArr=[]):
        self.node = node
        self.prefixArr = prefixArr


class Solution(object):

    def pathSum(self, root, target):
        if root == None:
            return 0
        count = 0
        stack = []
        stack.append(StackItem(root))
        while len(stack) > 0:
            pop = stack.pop()

            node = pop.node
            prefixArr = pop.prefixArr

            # add up the current value to the items in the prefix sum array
            newArr = []
            for s in prefixArr:
                temp = s + node.val
                newArr.append(temp)
                if temp == target:
                    count += 1
            # add the current value into the prefix sum array
            newArr.append(node.val)
            if node.val == target:
                count += 1

            # traverse down to its children
            if node.left != None:
                stack.append(StackItem(node.left, newArr))
            if node.right != None:
                stack.append(StackItem(node.right, newArr))
        return count
