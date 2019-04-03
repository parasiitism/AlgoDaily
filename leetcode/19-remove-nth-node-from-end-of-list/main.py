
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n <= 0:
            return head
        dump = ListNode(0)
        dump.next = head
        count = 0
        fast = dump
        while count < n and fast != None:
            fast = fast.next
            count += 1

        if fast == None:
            return head

        slow = dump
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dump.next
