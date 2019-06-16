"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

"""
    1st approach: recursion
    - get all the nodes. if a node has child, go into the child linked list
    - construct the linked list with the nodes in order

    Time    O(2n)
    Space   O(n)
    1460 ms, faster than 24.38%
"""


class Solution(object):

    def __init__(self):
        self.arr = []

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        self.dfs(head)
        dump = Node(0)
        cur = dump
        for i in range(len(self.arr)):
            x = self.arr[i]
            temp = Node(x, None, None, None)
            cur.next = temp
            if i > 0:
                temp.prev = cur
            cur = cur.next
        return dump.next

    def dfs(self, node):
        cur = node
        while cur != None:
            self.arr.append(cur.val)
            if cur.child != None:
                self.dfs(cur.child)
            cur = cur.next


"""
    2nd approach: recursion but dont create new nodes
    - get all the nodes. if a node has child, go into the child linked list
    - construct the linked list with the nodes in order

    Time    O(2n)
    Space   O(n)
    1148 ms, faster than 82.96%
"""


class Solution(object):

    def __init__(self):
        self.arr = []

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        self.dfs(head)
        dump = Node(0)
        cur = dump
        for i in range(len(self.arr)):
            x = self.arr[i]
            cur.next = x
            if i > 0:
                x.prev = cur
            x.child = None
            cur = cur.next
        return dump.next

    def dfs(self, node):
        cur = node
        while cur != None:
            self.arr.append(cur)
            if cur.child != None:
                self.dfs(cur.child)
            cur = cur.next
