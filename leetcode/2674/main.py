# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitCircularLinkedList(self, head: Optional[ListNode]) -> List[Optional[ListNode]]:
        """
        2 -> 4 -> 6 -> 8
        *    *
             ^         ^

        1 -> 3 -> 5 -> 7 -> 9
        *    *    *
             ^         ^
        """
        slow, fast = head, head.next
        while fast.next != head:
            slow = slow.next
            if fast.next.next != head:
                fast = fast.next.next
            else:
                fast = fast.next
        second_head = slow.next
        slow.next = head
        fast.next = second_head
        return [head, second_head]
