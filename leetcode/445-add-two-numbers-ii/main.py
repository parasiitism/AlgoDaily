# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
    1st approach: 2 stacks
	1. put the values into its corresponding stack
	2. pop the stacks, and sum up the numbers with carry
	3. if there is a carry, add 1

	Time	O(2m+2n)
	Space	O(m+n)
	16 ms, faster than 100.00%
"""


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        cur = l1
        while cur != None:
            stack1.append(cur.val)
            cur = cur.next
        cur = l2
        while cur != None:
            stack2.append(cur.val)
            cur = cur.next

        carry = 0
        dump = ListNode(0)
        while len(stack1) > 0 or len(stack2) > 0:
            # extract numbers
            val1 = 0
            if len(stack1) > 0:
                val1 = stack1.pop()
            val2 = 0
            if len(stack2) > 0:
                val2 = stack2.pop()
            # add them up
            combo = val1 + val2 + carry
            # construct new node and carry
            carry = combo/10
            newNode = ListNode(combo % 10)
            # reassign head
            temp = dump.next
            dump.next = newNode
            newNode.next = temp

        if carry > 0:
            newNode = ListNode(carry)
            # reassign head
            temp = dump.next
            dump.next = newNode
            newNode.next = temp
        return dump.next
