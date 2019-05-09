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
        # put values into stacks
        stack1 = []
        cur = l1
        while cur != None:
            stack1.append(cur.val)
            cur = cur.next
        stack2 = []
        cur = l2
        while cur != None:
            stack2.append(cur.val)
            cur = cur.next
        # start from a dump node
        dump = ListNode(-1)
        carry = 0
        # pop the stacks
        while len(stack1) > 0 or len(stack2) > 0:
            a = 0
            if len(stack1) > 0:
                a = stack1.pop()
            b = 0
            if len(stack2) > 0:
                b = stack2.pop()
            temp = a + b + carry
            carry = temp/10
            num = temp%10
            node = ListNode(num)
            node.next = dump.next
            dump.next = node
        # if unfortunately there is an extra one
        if carry > 0:
            node = ListNode(1)
            node.next = dump.next
            dump.next = node
        return dump.next
