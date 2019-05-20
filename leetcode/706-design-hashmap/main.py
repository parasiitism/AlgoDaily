"""
    2nd approach:
    - 1000 buckets
    - each bucket has 1000 slots

    however, there is a limition of total number of items inserted into the hashtable

    828 ms beats 13.40%
    1apr2019
"""


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 1000 buckets
        # each bucket has 1000 slots
        self.buckets = []
        for i in range(1000):
            self.buckets.append(1000*[-1])

    def _getBucket(self, num):
        return num / 1000

    def _getSlot(self, num):
        return num % 1000

    def put(self, key, value):
        """
        :type key: int
        :rtype: None
        """
        b = self._getBucket(key)
        s = self._getSlot(key)
        self.buckets[b][s] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        b = self._getBucket(key)
        s = self._getSlot(key)
        return self.buckets[b][s]

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        b = self._getBucket(key)
        s = self._getSlot(key)
        self.buckets[b][s] = -1


"""
    3rd approach:
    - linked list chaining 

    advantage: no limitation of total number of key&value pairs

    although it gets TLE on leetcode, it is a decent and pragmatic approach to deal with hash collision
"""


class ListNode(object):

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap(object):

    def __init__(self):
        self.buckets = 1000*[ListNode(-1, None)]

    def _getBucket(self, num):
        return self.buckets[int(num/1000)]

    def put(self, key, value):
        """
        :type key: int
        :rtype: None
        """
        head = self._getBucket(key)
        prev = head
        cur = prev.next
        while cur != None:
            if cur.key == key:
                cur.val = value
                return
            prev = cur
            cur = cur.next
        prev.next = ListNode(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        head = self._getBucket(key)
        cur = head.next
        while cur != None:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

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
                return
            prev = cur
            cur = cur.next


hs = MyHashMap()
hs.put(1, 1)
hs.put(2, 2)
hs.put(3, 3)
print(hs.get(1))
print(hs.get(2))
print(hs.get(3))
hs.put(2, 20)
print(hs.get(1))
print(hs.get(2))
print(hs.get(3))
hs.remove(2)
print(hs.get(1))
print(hs.get(2))
print(hs.get(3))
hs.put(3, 30)
print(hs.get(1))
print(hs.get(2))
print(hs.get(3))
