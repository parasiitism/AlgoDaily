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
        dump = ListNode(-1)
        dump.next = head
        cur = dump
        while cur != None and cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dump.next
