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
        O(n/2)
        """
        s = []
        half = int(self.count/2)+1

        def inorderBst(node):
            nonlocal half
            if node == None:
                return
            inorderBst(node.left)
            for i in range(node.count):
                if half <= 0:
                    return
                s.append(node.val)
                half -= 1
            inorderBst(node.right)
        inorderBst(self.bst)

        if self.count == 0:
            return 0
        elif self.count % 2 == 0:
            return float(s[-2]+s[-1])/2.0
        else:
            return s[-1]

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


obj = MedianFinder()
obj.addNum(1)
print(obj.findMedian())

print("---")

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())

print("---")

obj = MedianFinder()
obj.addNum(1)
obj.addNum(3)
obj.addNum(2)
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
print(obj.findMedian())
