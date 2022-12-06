# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    Stack
    - the next larger element

    Time    O(N)
    Space   O(N)
    1923 ms, faster than 78.52%
"""


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head
        while cur != None:
            while len(stack) > 0 and cur.val > stack[-1]:
                stack.pop()
            stack.append(cur.val)
            cur = cur.next

        dumb = ListNode()
        cur = dumb
        for x in stack:
            cur.next = ListNode(x)
            cur = cur.next
        return dumb.next
