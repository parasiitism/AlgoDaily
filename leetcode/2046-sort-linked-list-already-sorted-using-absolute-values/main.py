"""
    1st: linked list
    - extract the values into 2 linked lists: positives and negatives
    - reverse the negative linked list and put it to the front

    Time    O(N)
    Space   O(N) the result linked list
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        positiveHead = ListNode()
        negativeHead = ListNode()
        positiveCur = positiveHead
        negativeCur = negativeHead
        cur = head
        while cur != None:
            if cur.val >= 0:
                positiveCur.next = ListNode(cur.val)
                positiveCur = positiveCur.next
            else:
                negativeCur.next = ListNode(cur.val)
                negativeCur = negativeCur.next
            cur = cur.next

        resHead = ListNode()
        if negativeHead.next != None:
            resHead.next = self.reverseList(negativeHead.next)
        cur = resHead
        while cur.next != None:
            cur = cur.next
        cur.next = positiveHead.next
        return resHead.next

    def reverseList(self, head: ListNode) -> ListNode:
        newHead = head
        while head != None and head.next != None:
            temp = head.next
            head.next = head.next.next
            temp.next = newHead
            newHead = temp
        return newHead
