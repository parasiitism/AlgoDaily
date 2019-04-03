# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
    2nd approach: same idea as 1st approach but shorter

	Time	O(l+r)
	Space	O(l+r) the result
	12ms beats 100%
"""


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        cur1 = l1
        cur2 = l2
        dump = ListNode(0)
        cur = dump
        while cur1 != None or cur2 != None:
            # extract numbers
            val1 = 0
            if cur1 != None:
                val1 = cur1.val
            val2 = 0
            if cur2 != None:
                val2 = cur2.val
            # add them up
            combo = val1 + val2 + carry
            # construct new node and carry
            carry = combo/10
            node = ListNode(combo % 10)
            cur.next = node
            # iterate
            cur = cur.next
            if cur1 != None:
                cur1 = cur1.next
            if cur2 != None:
                cur2 = cur2.next
        if carry > 0:
            cur.next = ListNode(1)
        return dump.next
