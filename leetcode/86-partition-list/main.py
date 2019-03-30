# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode

        1st approach:
        - create 2 linked lists: 1 for nodes less than target, 1 for nodes >= target
        - put the nodes into the corresponding lists while we traversing the input
        - combine the 2 linked lists and return the result

        Time    O(n)
        Space   O(n)
        28 ms, faster than 27.58%
        """
        dumpLess = ListNode(0)
        dumpMore = ListNode(0)
        curLess = dumpLess
        curMore = dumpMore
        cur = head
        while cur != None:
            if cur.val < x:
                temp = ListNode(cur.val)
                curLess.next = temp
                curLess = curLess.next
            else:
                temp = ListNode(cur.val)
                curMore.next = temp
                curMore = curMore.next
            cur = cur.next
        curLess.next = dumpMore.next
        return dumpLess.next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode

        2nd approach:
        - create 2 linked lists: 1 for nodes less than target, 1 for nodes >= target
        - put the nodes into the corresponding lists while we traversing the input
        - combine the 2 linked lists and return the result

        Time    O(n)
        Space   O(1)
        36 ms, faster than 13.88%
        """
        dumpLess = ListNode(0)
        dumpMore = ListNode(0)
        curLess = dumpLess
        curMore = dumpMore
        cur = head
        while cur != None:
            if cur.val < x:
                curLess.next = cur
                curLess = curLess.next
            else:
                curMore.next = cur
                curMore = curMore.next
            cur = cur.next
        # very important:
        # since, after the traversal, curMore.next points to the curLess node
        # we should set the next to null to avoid creating a cyclar linked list
        # e.g. [1,4,3,2]
        # dumpLess -> 1,2
        # dumpMore -> 4,3,2
        curMore.next = None
        curLess.next = dumpMore.next
        return dumpLess.next


# helper
def printList(root):
    cur = root
    while cur != None:
        print(cur.val)
        cur = cur.next


a = ListNode(1)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
a.next = b
b.next = c
c.next = d
ans = Solution().partition(a, 3)
printList(ans)
