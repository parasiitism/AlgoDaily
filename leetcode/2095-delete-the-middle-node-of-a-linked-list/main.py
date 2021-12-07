# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    1st: 2 pointers

    Time    O(N)
    Space   O(1)
    1812 ms, faster than 14.29%
"""


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dumbhead = ListNode(-1, head)
        slow = dumbhead
        fast = dumbhead
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return dumbhead.next
