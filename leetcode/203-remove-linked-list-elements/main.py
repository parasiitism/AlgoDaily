"""
    1st approach
    - remove the next pointer if it contains the target in a loop

    Time    (n)
    Space   O(1)
    56 ms, faster than 100.00%
"""


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dump = ListNode(-1)
        dump.next = head
        cur = dump
        while cur != None:
            while cur.next != None and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
        return dump.next


"""
    classic approach
    - remove the next pointer if it contains the target

    Time    (n)
    Space   O(1)
    56 ms, faster than 100.00%
"""


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dump = ListNode(0)
        dump.next = head
        prev = dump
        cur = head
        while cur != None:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dump.next
