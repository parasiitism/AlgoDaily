# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    1st: pointer
    
    Time    O(N)
    Space   O(N)
    4658 ms, faster than 20.00%
"""


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        newCur = newHead
        cur = head.next
        pfs = 0
        while cur != None:
            if cur.val != 0:
                pfs += cur.val
            else:
                newCur.next = ListNode(pfs)
                newCur = newCur.next
                pfs = 0
            cur = cur.next
        return newHead.next
