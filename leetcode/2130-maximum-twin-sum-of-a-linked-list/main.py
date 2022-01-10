# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    1st: linked list
    - transform to an array
    - 2 pointers

    Time    O(2N)
    Space   O(N) the array
    996 ms, faster than 16.67%
"""


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = self.ll2arr(head)
        res = 0
        i, j = 0, len(arr)-1
        while i < j:
            res = max(res, arr[i] + arr[j])
            i += 1
            j -= 1
        return res

    def ll2arr(self, head):
        arr = []
        cur = head
        while cur != None:
            arr.append(cur.val)
            cur = cur.next
        return arr
