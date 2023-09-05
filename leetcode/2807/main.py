"""
    linked list

    Time    O(N)
    Space   O(1)
"""


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur != None and cur.next != None:
            nxt = cur.next
            gcd = math.gcd(cur.val, nxt.val)
            gcd_node = ListNode(gcd)
            cur.next = gcd_node
            gcd_node.next = nxt
            cur = nxt
        return head
