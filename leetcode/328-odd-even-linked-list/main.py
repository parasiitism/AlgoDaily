# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    navie solution
	- put the items into even and odd arrays
	- concat them together

	time		O(n)
	space	O(n)
	beats 100% (LOL the speed is the same with the classic approach)
"""


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddList = ListNode(0)
        evenList = ListNode(0)
        cur = head
        oddCur = oddList
        evenCur = evenList
        i = 1
        while cur != None:
            if i % 2 == 0:
                evenCur.next = ListNode(cur.val)
                evenCur = evenCur.next
            else:
                oddCur.next = ListNode(cur.val)
                oddCur = oddCur.next
            cur = cur.next
            i += 1
        oddCur.next = evenList.next
        return oddList.next


"""
    navie solution
	- put the items into even and odd arrays
	- concat them together

	time		O(n)
	space	O(n)
	beats 100% (LOL the speed is the same with the classic approach)
"""


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddList = ListNode(0)
        evenList = ListNode(0)
        cur = head
        oddCur = oddList
        evenCur = evenList
        i = 1
        while cur != None:
            if i % 2 == 0:
                evenCur.next = cur
                evenCur = evenCur.next
            else:
                oddCur.next = cur
                oddCur = oddCur.next
            cur = cur.next
            i += 1
        oddCur.next = evenList.next
        evenCur.next = None
        return oddList.next
