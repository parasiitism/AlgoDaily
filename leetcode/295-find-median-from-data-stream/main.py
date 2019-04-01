import heapq

"""
    1st approach: heap
    - LTE
"""


class MedianFinder(object):

    def __init__(self):
        self.pq = []

    def addNum(self, num):
        """
        O(logn)
        """
        heapq.heappush(self.pq, num)

    def findMedian(self):
        """
        O(klogn)
        """
        if len(self.pq) == 0:
            return 0
        elif len(self.pq) % 2 == 0:
            firstHalf = self.getFirstHalf()
            return float(firstHalf[-2]+firstHalf[-1])/2.0
        else:
            firstHalf = self.getFirstHalf()
            return firstHalf[-1]

    def getFirstHalf(self):
        clone = self.pq[:]
        half = len(self.pq)/2+1
        res = []
        for i in range(half):
            temp = heapq.heappop(clone)
            res.append(temp)
        return res


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(1)
# print(obj.findMedian())

# print("---")

# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# print(obj.findMedian())

# print("---")

# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(3)
# obj.addNum(2)
# print(obj.findMedian())

# print("---")

# obj = MedianFinder()
# obj.addNum(5)
# obj.addNum(3)
# obj.addNum(4)
# obj.addNum(3)
# obj.addNum(1)
# obj.addNum(2)
# obj.addNum(6)
# print(obj.findMedian())


"""
    2nd approach: BST
    - LTE
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count = 1


class MedianFinder(object):

    def __init__(self):
        self.bst = None
        self.count = 0
        self.sortedList = []

    def addNum(self, num):
        """
        O(logn)
        """
        self.count += 1
        if self.bst == None:
            self.bst = TreeNode(num)
            return
        self.insertIntoBST(self.bst, num)

    def findMedian(self):
        """
        O(n)
        """
        self.sortedList = []
        self.inorderBst(self.bst)
        half = self.count/2
        if self.count == 0:
            return 0
        elif self.count % 2 == 0:
            return float(self.sortedList[half-1]+self.sortedList[half])/2.0
        else:
            return self.sortedList[half]

    def insertIntoBST(self, root, num):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if num == root.val:
            root.count += 1
        elif num < root.val:
            if root.left == None:
                root.left = TreeNode(num)
            else:
                self.insertIntoBST(root.left, num)
        else:
            if root.right == None:
                root.right = TreeNode(num)
            else:
                self.insertIntoBST(root.right, num)

    def inorderBst(self, node):
        if node == None:
            return
        self.inorderBst(node.left)
        self.sortedList += node.count*[node.val]
        self.inorderBst(node.right)


# obj = MedianFinder()
# obj.addNum(1)
# print(obj.findMedian())

# print("---")

# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# print(obj.findMedian())

# print("---")

# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(3)
# obj.addNum(2)
# print(obj.findMedian())

# print("---")

# obj = MedianFinder()
# obj.addNum(5)
# obj.addNum(3)
# obj.addNum(4)
# obj.addNum(3)
# obj.addNum(1)
# obj.addNum(2)
# obj.addNum(6)
# print(obj.findMedian())

"""
    3rd approach: 2 heaps
    - maxheap for left half
    - minheap for right half
    - therefore the mean will always be the max of maxheap and the min of minheap
    - https://leetcode.com/articles/find-median-from-data-stream/

    336 ms, faster than 48.83%
"""


class MedianFinder(object):

    def __init__(self):
        # for left half
        self.maxheap = []
        # for right half
        self.minheap = []

    def addNum(self, num):
        """
        O(3*logn)
        """
        if len(self.maxheap) == len(self.minheap):
            heapq.heappush(self.maxheap, -num)
            largest = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -largest)
        else:
            heapq.heappush(self.minheap, num)
            least = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -least)

    def findMedian(self):
        """
        O(1)
        """
        if len(self.maxheap) != len(self.minheap):
            return self.minheap[0]
        return (-self.maxheap[0] + self.minheap[0])/2.0


obj = MedianFinder()
obj.addNum(1)
print(obj.maxheap)
print(obj.minheap)
print(obj.findMedian())

print("---")

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.maxheap)
print(obj.minheap)
print(obj.findMedian())

print("---")

obj = MedianFinder()
obj.addNum(1)
obj.addNum(3)
obj.addNum(2)
print(obj.maxheap)
print(obj.minheap)
print(obj.findMedian())

print("---")

obj = MedianFinder()
obj.addNum(5)
obj.addNum(3)
obj.addNum(4)
obj.addNum(3)
obj.addNum(1)
obj.addNum(2)
obj.addNum(6)
print(obj.maxheap)
print(obj.minheap)
print(obj.findMedian())


print("========================================")
