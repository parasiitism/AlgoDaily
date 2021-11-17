
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    1st: linked list
    - it is too annoying to use 2 pointers to implement, use an array instead

    Time    O(N)
    Space   O(N)
    3584 ms, faster than 31.76% 
"""


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = self.linkedList2Nums(head)
        res = []
        i = 0
        natural = 1
        while i < len(nums):
            sub = nums[i:i+natural]
            if len(sub) % 2 == 1:
                res += sub
            else:
                res += sub[::-1]
            i += natural
            natural += 1

        return self.nums2LinkedList(res)

    def linkedList2Nums(self, head):
        nums = []
        cur = head
        while cur != None:
            nums.append(cur.val)
            cur = cur.next
        return nums

    def nums2LinkedList(self, nums):
        dumphaed = ListNode()
        cur = dumphaed
        for x in nums:
            cur.next = ListNode(x)
            cur = cur.next
        return dumphaed.next
