# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode

        1st approach
        - similar to reverse linked list and reverse halh of a linked list
        - we need to find the parent of node[m] first, reverse the later list until the count < n(right)
        20ms beats 100%
        29jan2019
        """
        # find the parent of node[m]
        dump = ListNode(0)
        dump.next = head
        i = 1
        parent = dump
        while i < m and parent != None:
            i += 1
            parent = parent.next

        # reverse the linked list until n
        targetHead = parent.next
        cur = targetHead
        while i < n and targetHead.next != None:
            temp = targetHead.next
            targetHead.next = targetHead.next.next
            temp.next = cur
            cur = temp
            i += 1
        parent.next = cur
        return dump.next


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
        acc += str(c.val)+','
        c = c.next
    print(acc)


a = arr2list([])
s = Solution().reverseBetween(a, 0, 0)
printList(s)

a = arr2list([1])
s = Solution().reverseBetween(a, 1, 1)
printList(s)

a = arr2list([1, 2, 3, 4, 5])
s = Solution().reverseBetween(a, 2, 4)
printList(s)

a = arr2list([1, 2, 3, 4, 5])
s = Solution().reverseBetween(a, 2, 5)
printList(s)

a = arr2list([1, 2, 3, 4, 5])
s = Solution().reverseBetween(a, 1, 4)
printList(s)

a = arr2list([1, 2, 3, 4, 5])
s = Solution().reverseBetween(a, 1, 5)
printList(s)
