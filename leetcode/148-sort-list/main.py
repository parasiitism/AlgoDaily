# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    2nd approach: merge sort

    Time    O(n)
    Space   O(n)
    268 ms, faster than 22.26%
"""


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        rightHalf = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(rightHalf)
        return self.merge(left, right)

    def merge(self, a, b):
        dump = ListNode(0)
        cur = dump
        curA = a
        curB = b
        while curA != None and curB != None:
            if curA.val < curB.val:
                cur.next = curA
                curA = curA.next
            else:
                cur.next = curB
                curB = curB.next
            cur = cur.next
        if curA != None:
            cur.next = curA
        if curB != None:
            cur.next = curB
        return dump.next
