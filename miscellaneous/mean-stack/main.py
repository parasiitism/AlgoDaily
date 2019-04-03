"""
Mean Stack 

push        O(logn)
pop         O(logn)
top        O(1)
peekMean    O(1)
popMean     O(logn)
P.S. only pop the left if there are 2 in the middle
"""


class DLLNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MeanStack(object):

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
        # append to tail
        last = self.tail.prev
        node = DLLNode(x)
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node
        # binary search to insert the number
        idx = self.upper_bsearch(self.nums, x)
        self.nums.insert(idx, (x, node))

    def pop(self):
        """
        :rtype: int
        """
        last = self.tail.prev
        last.prev.next = last.next
        last.next.prev = last.prev
        # binary search to remove the node
        idx = self.upper_bsearch(self.nums, last.val)
        self.nums.pop(idx-1)
        return last.val

    def top(self):
        """
        :rtype: int
        """
        return self.tail.prev.val

    def peekMean(self):
        """
        :rtype: float
        """
        # calculate the mean
        m = (len(self.nums)-1)/2
        if len(self.nums) % 2 == 1:
            return self.nums[m][0]
        return (self.nums[m][0] + self.nums[m+1][0])/2

    def popMean(self):
        """
        :rtype: float
        """
        m = (len(self.nums)-1)/2
        # calculate the mean
        result = 0
        if len(self.nums) % 2 == 1:
            result = self.nums[m][0]
        else:
            result = (self.nums[m][0] + self.nums[m+1][0])/2
        # remove the mean node
        # if the total number of nodes is even, remove the left in the middle
        meanVal, meanNode = self.nums[m]
        meanNode.prev.next = meanNode.next
        meanNode.next.prev = meanNode.prev
        # binary search to remove the node
        idx = self.upper_bsearch(self.nums, meanVal)
        self.nums.pop(idx-1)

        return result

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
