# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    1st approach: arr
    - put all the values(!= target) into an array
    - override the values in the linked list
    - last node points to null

    Time    O(2n)
    Space   O(n)
    24 ms, faster than 89.05%
"""


class Solution(object):
    def deleteNode(self, head, n):
        """
        :type node: ListNode
        :type n: int
        :rtype: None Do not return anything, modify node in-place instead.
        """
        arr = []
        cur = head
        while cur != None:
            if cur.val != n:
                arr.append(cur.val)
            cur = cur.next
        cur = head
        for i in range(len(arr)):
            cur.val = arr[i]
            if i+1 < len(arr):
                cur = cur.next
            else:
                cur.next = None
