# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    1st approach: hashtable
    - put alll the G items into the hashset
    - for each node, check if it is in the hashset, if yes, increment the connectedCount
    - if no and there are items previously, increment the result
    - result is the result

    Time    O(n)
    Space   O(n)
    104 ms, faster than 63.04%
"""


class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        # put alll the G items into the hashset
        hs = set(G)
        count = 0
        connectedCount = 0
        # traverse the linked list
        cur = head
        while cur != None:
            if cur.val in hs:
                # add to the arr
                connectedCount += 1
            elif connectedCount > 0:
                # if len(arr) > 0, it means we have item(s) previously
                count += 1
                connectedCount = 0
            # traversal
            cur = cur.next
        # corner test when the last item is in the set
        if connectedCount > 0:
            count += 1
        return count
