"""
    1st approach: math
    - If there are N nodes in the list, and k parts, then every part has N/k elements, except the first N%k parts have an extra one

    Time    O(2N)
    Space   O(n)
    44 ms, faster than 9.85%
"""


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        # get the number of nodes in linked list
        count = 0
        cur = root
        while cur != None:
            count += 1
            cur = cur.next
        # kPlusOne means the number of the items that the linked list should be with length count/k+1
        kPlusOne = count % k
        cur = root
        res = []
        for i in range(k):
            dump = ListNode(0)
            dumpCur = dump
            c = 0
            # supposedly the number of nodes in linked list should be count/k
            # but for index < kPlusOne, the length should be count/k+1
            limit = count/k
            if i < kPlusOne:
                limit += 1
            # traverse and add nodes in linked lists
            while cur != None and c < limit:
                dumpCur.next = cur
                dumpCur = dumpCur.next
                cur = cur.next
                c += 1
            # dont forget to cut the linked list
            dumpCur.next = None
            res.append(dump.next)
        return res
