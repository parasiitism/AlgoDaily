
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    1st: linked list, math?
    - traverse the linked list and put items in an array
    - find the critical points
    - maxDiff = the diff between the first and the last
    - minDiff = the min diff between any adjacent numbers 
"""


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        cur = head
        while cur != None:
            nums.append(cur.val)
            cur = cur.next
        points = []
        for i in range(1, len(nums)-1):
            left = nums[i-1]
            x = nums[i]
            right = nums[i+1]
            if x < left and x < right:
                points.append(i)
            elif x > left and x > right:
                points.append(i)
        if len(points) <= 1:
            return [-1, -1]
        maxDiff = points[-1] - points[0]
        minDiff = 2**32
        for i in range(1, len(points)):
            diff = points[i] - points[i-1]
            minDiff = min(minDiff, diff)
        return [minDiff, maxDiff]
