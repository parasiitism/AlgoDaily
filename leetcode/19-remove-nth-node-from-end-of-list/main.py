
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
    1st approach: 2 pointers + dump
    - the gap is the n such that when fast reaches to the end, slow.next is the target

    e.g. 
    
    list = 1 -> 2 -> 3 -> 4 -> 5, target = 4
    
    1 -> 2 -> 3 -> 4 -> 5
              ^         ^
            slow        fast

    Time		O(n+target)
    Space       O(1)
    24 ms, faster than 72.46%
"""


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

        # in case if n > length of linked list, we just remove the head
        if fast == None or fast.next == None:
            return head.next

        slow = dump
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dump.next


"""
    2nd approach: 2 pointers without using dump
    - the gap is the n such that when fast reaches to the end, slow.next is the target

    Time		O(n+target)
    Space       O(1)
    20 ms, faster than 96.68%
"""


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n <= 0:
            return head
        fast = head
        for _ in range(n):
            fast = fast.next
            if fast == None:
                break
        # it means the nth points to the head
        if fast == None:
            return head.next
        # traverse
        slow = head
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
