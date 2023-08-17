from collections import *
"""
    Doubly Linked List + Hashtable
    - similar to lc379, lc1429

    Time  put:O(1), get: O(1)
    124ms beats 96.42%
"""


class LLNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.head = LLNode()
        self.tail = LLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.ht = {}

    def _removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _addToTail(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.ht:
            return -1
        node = self.ht[key]
        self._removeNode(node)
        self._addToTail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.ht:
            node = LLNode(key, value)
            self._addToTail(node)
            self.ht[key] = node
            self.size += 1
        else:
            node = self.ht[key]
            node.val = value
            self._removeNode(node)
            self._addToTail(node)
        if self.size > self.cap:
            first = self.head.next
            self._removeNode(first)
            del self.ht[first.key]
            self.size -= 1


c = LRUCache(2)
c.put("c", 123)
c.put("a", 456)
c.put("b", 789)
print(c.map)
c.put("a", 123)
print(c.listHead)
c.get("b")
c.get("b")
c.get("b")
print(c.listHead)

"""
    2nd approach: use orderdict

    Time of put():    O(1)
    Time of get():    O(1)
    940 ms, faster than 6.85%
"""


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.od = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.od:
            v = self.od[key]
            del self.od[key]
            self.od[key] = v
            return v
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.od:
            del self.od[key]
            self.od[key] = value
        else:
            self.od[key] = value
            if len(self.od) > self.capacity:
                firstKey = None
                for key in self.od:
                    firstKey = key
                    break
                del self.od[firstKey]


c = LRUCache(2)
c.put("c", 123)
c.put("a", 456)
c.put("b", 789)
print(c.od)
c.put("a", 123)
print(c.od)
c.get("b")
c.get("b")
c.get("b")
print(c.od)
