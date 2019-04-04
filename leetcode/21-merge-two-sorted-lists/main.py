"""
    Merge two sorted linked lists and return it as a new list. 
    The new list should be made by splicing together the nodes of the first two lists.

    Time    O(A+B)
    Space   O(A+B)
    28 ms, faster than 64.53%
"""


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def merge2Lists(self, l1, l2):
        """
            Time
            24ms beats 100%
        """
        dumphead = ListNode(0)
        cur = dumphead
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2
        return dumphead.next


# helpers for test
def arr2list(arr):
    dump = ListNode(0)
    dumpCur = dump
    for i in range(len(arr)):
        dumpCur.next = ListNode(arr[i])
        dumpCur = dumpCur.next
    return dump.next


def printList(l):
    c = l
    acc = ""
    while c != None:
        acc += str(c.val) + ','
        c = c.next
    print(acc)


a = arr2list([1, 3, 5])
b = arr2list([2, 4, 6])
s = Solution().merge2Lists(a, b)
printList(s)

a = arr2list([1, 3, 5])
b = arr2list([2, 4, 5, 6])
s = Solution().merge2Lists(a, b)
printList(s)
