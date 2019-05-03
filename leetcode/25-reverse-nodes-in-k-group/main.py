# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    2nd approach: 2 pointers
    - 1st faster to count if there are enough nodes ahead
    - 2nd slower to stay and
        - if there are enoguh nodes ahead, reverse the nodes until we reach to the fast pointer
    
    Time    O(n)
    Space   O(1)
    40ms beats 63.34%
    3may2019
"""


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dump = ListNode(0)
        dump.next = head
        slow = dump
        fast = dump
        while True:
            count = 0
            while fast != None and fast.next != None and count < k:
                fast = fast.next
                count += 1
            if count != k:
                break
            else:
                temp = slow.next
                # at the begining
                # slow is the dump, fast is the node at count = k
                slow.next = self.reverse(slow.next, fast.next)
                fast = temp
                slow = temp
        return dump.next

    def reverse(self, head, fast):
        newHead = head
        while head.next != fast:
            temp = head.next
            head.next = head.next.next
            temp.next = newHead
            newHead = temp
        return newHead
