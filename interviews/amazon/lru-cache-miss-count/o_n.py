"""
    A hit means the requested page is already existing in the cache 
    and a miss means the requested page is not found in the cache
"""


class ListNode(object):

    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


def countMiss(nums, k):
    """
        2nd approach:
        - hashtable + doubly linked list to optimize put() operation
        Time    O(n)
        Space   O(n)
    """
    cache = {}
    listHead = ListNode(-1)
    listTail = ListNode(-1)
    listHead.next = listTail
    listTail.prev = listHead
    listLength = 0

    count = 0

    for num in nums:

        if num in cache:
            # remove target from current position
            target = cache[num]
            target.prev.next = target.next
            target.next.prev = target.prev
            listLength -= 1
        else:
            count += 1
            # remove head if needed
            if k == listLength:
                first = listHead.next
                listHead.next = first.next
                first.next.prev = listHead
                # remove cache
                del cache[first.key]
                listLength -= 1

        # add to tail
        node = ListNode(num)
        last = listTail.prev
        last.next = node
        node.prev = last
        node.next = listTail
        listTail.prev = node
        # add cache
        cache[num] = node
        listLength += 1

    return count


print(countMiss([1, 2, 3, 4, 5, 4, 1], 4))
print(countMiss([1, 2, 3, 4, 5, 4, 3, 2, 5, 6], 3))
