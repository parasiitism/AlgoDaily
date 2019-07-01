"""
    2nd approach:
    - 1000 buckets
    - each bucket has 1000 slots

    however, there is a limition of total number of items inserted into the hashtable

     624 ms beats 17.74%
    1apr2019
"""


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 1000 buckets
        # each bucket has 1000 slots
        self.buckets = []
        for i in range(1000):
            self.buckets.append(1000*[False])

    def _getBucket(self, num):
        return num//1000

    def _getSlot(self, num):
        return num % 1000

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        b = self._getBucket(key)
        s = self._getSlot(key)
        self.buckets[b][s] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        b = self._getBucket(key)
        s = self._getSlot(key)
        self.buckets[b][s] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        b = self._getBucket(key)
        s = self._getSlot(key)
        return self.buckets[b][s]


"""
    3rd approach:
    - linked list chaining

    advantage: no limitation of total number of key&value pairs

    although it gets TLE on leetcode, it is a decent and pragmatic approach to deal with hash collision
"""


class ListNode(object):

    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet(object):

    def __init__(self):
        self.buckets = 1000*[ListNode(-1)]

    def _getBucket(self, num):
        return self.buckets[num//1000]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        head = self._getBucket(key)
        prev = head
        cur = prev.next
        while cur != None:
            if cur.key == key:
                return
            prev = cur
            cur = cur.next
        prev.next = ListNode(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        head = self._getBucket(key)
        prev = head
        cur = prev.next
        while cur != None:
            if cur.key == key:
                prev.next = cur.next
            prev = cur
            cur = cur.next

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        head = self._getBucket(key)
        cur = head.next
        while cur != None:
            if cur.key == key:
                return True
            cur = cur.next
        return False


hs = MyHashSet()
hs.add(1)
hs.add(2)
hs.add(3)
print(hs.contains(1))
print(hs.contains(2))
print(hs.contains(3))
hs.add(2)
hs.remove(2)
print(hs.contains(2))
