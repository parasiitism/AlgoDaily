"""
    2nd approach: doubly linked list + binary search

    Time
    - push      O(logn)
    - pop       O(logn)
    - top       O(1)
    - peekMax   O(1)
    - popMax    O(logn)
    256 ms, faster than 17.40%
"""


class DLLNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.head = DLLNode(0)
        self.tail = DLLNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        last = self.tail.prev
        node = DLLNode(x)
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

        idx = self.upper_bsearch(self.nums, x)
        self.nums.insert(idx, (x, node))

    def pop(self):
        """
        :rtype: int
        """
        last = self.tail.prev
        last.prev.next = last.next
        last.next.prev = last.prev

        idx = self.upper_bsearch(self.nums, last.val)
        self.nums.pop(idx-1)
        return last.val

    def top(self):
        """
        :rtype: int
        """
        return self.tail.prev.val

    def peekMax(self):
        """
        :rtype: int
        """
        return self.nums[-1][0]

    def popMax(self):
        """
        :rtype: int
        """
        maxVal, maxNode = self.nums[-1]
        maxNode.prev.next = maxNode.next
        maxNode.next.prev = maxNode.prev

        idx = self.upper_bsearch(self.nums, maxVal)
        self.nums.pop(idx-1)
        return maxVal

    def upper_bsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)/2
            if target >= nums[mid][0]:
                left = mid + 1
            else:
                right = mid
        return left
