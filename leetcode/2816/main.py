"""
    1st:
    - reverse linked list
    - cur.val * 2 + carry
    - reverse the linked list again and ppend the carry if necessary

    Time    O(N)
    Space   O(1)
"""


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverseHead = self.reverse(head)
        cur = reverseHead
        carry = 0
        while cur != None:
            temp = cur.val * 2 + carry
            cur.val = temp % 10
            carry = temp // 10
            cur = cur.next
        if carry > 0:
            return ListNode(carry, self.reverse(reverseHead))
        return self.reverse(reverseHead)

    def reverse(self, head):
        cur = head
        while cur != None and cur.next != None:
            temp = cur.next
            cur.next = cur.next.next
            temp.next = head
            head = temp
        return head
