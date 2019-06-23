# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    easier to understand the classic approach
	1. check if there is a cycle
	2. slow pointer => a+b+c+b= 2(a+b) <= fast pointer
														a=c
	see ./idea.jpeg
	time 	O(n)
	space	O(1)
	40 ms, faster than 86.31%
"""


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast == None or fast.next == None:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
