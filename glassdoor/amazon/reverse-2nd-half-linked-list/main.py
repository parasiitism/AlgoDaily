"""
  reverse second half of a linked list
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseSecondHalf(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        1st approach
        - use a dump head
        """
        if head == None:
            return None
        # very important:
        # find the midpoint's parent instead of the midpoint
        # such that we can mutate the 2nd half
        dump = ListNode(0)
        dump.next = head
        slow = dump
        fast = head
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        # print(slow.val)

        # reverse the 2nd half
        targetList = slow.next
        dump = ListNode(0)
        dump.next = targetList
        striker = targetList.next
        while striker != None:
            temp = dump.next
            dump.next = striker
            targetList.next = striker.next
            striker.next = temp
            striker = targetList.next
        slow.next = dump.next
        return head


class Solution1(object):
    def reverseSecondHalf(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        1st approach
        - mutate the slow pointer directly
        """
        if head == None:
            return None
        # very important:
        # find the midpoint's parent instead of the midpoint
        # such that we can mutate the 2nd half
        dump = ListNode(0)
        dump.next = head
        slow = dump
        fast = head
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half
        targetHead = slow.next
        cur = targetHead
        while targetHead.next != None:
            temp = targetHead.next
            targetHead.next = targetHead.next.next
            temp.next = cur
            cur = temp
        slow.next = cur
        return head


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
s = Solution1().reverseSecondHalf(a)
printList(s)

a = arr2list([1])
s = Solution1().reverseSecondHalf(a)
printList(s)

a = arr2list([1, 2])
s = Solution1().reverseSecondHalf(a)
printList(s)

a = arr2list([1, 2, 3])
s = Solution1().reverseSecondHalf(a)
printList(s)

a = arr2list([1, 2, 3, 4, 5])
s = Solution1().reverseSecondHalf(a)
printList(s)

a = arr2list([1, 2, 3, 4, 5, 6])
s = Solution1().reverseSecondHalf(a)
printList(s)

a = arr2list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
s = Solution1().reverseSecondHalf(a)
printList(s)
