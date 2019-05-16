# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        m = set()
        cur = headA
        while cur != None:
            m.add(cur)
            cur = cur.next
        cur = headB
        while cur != None:
            if cur in m:
                return cur
            cur = cur.next
        return None
