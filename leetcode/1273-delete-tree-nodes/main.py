"""
    1st: recursion
    - contruct a tree with a hashtbale(because there will be no duplicate keys)
    - count the sum and reconstruct the tree with the case sum == 0
    - count the number of nodes in the remaining tree

    Time    O(3N)
    Space   O(N)
    312 ms, faster than 9.47%
"""


class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.children = []


class Solution(object):
    def deleteTreeNodes(self, nodes, parent, value):
        """
        :type nodes: int
        :type parent: List[int]
        :type value: List[int]
        :rtype: int
        """
        ht = {}
        ht[0] = Node(0, value[0])
        for i in range(1, nodes):
            node = Node(i, value[i])
            parentIdx = parent[i]
            ht[parentIdx].children.append(node)
            ht[i] = node
        newTree, _ = self.dfs(ht[0])
        return self.countNodes(newTree)

    def dfs(self, node):
        if node == None:
            return None, 0
        total = node.val
        newChildren = []
        for child in node.children:
            tempChild, tempTotal = self.dfs(child)
            if tempTotal != 0:
                newChildren.append(tempChild)
                total += tempTotal
        if total == 0:
            return None, 0
        node.children = newChildren
        return node, total

    def countNodes(self, node):
        if node == None:
            return 0
        total = 1
        for child in node.children:
            total += self.countNodes(child)
        return total
