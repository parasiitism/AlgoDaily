class ListNode(object):
    def __init__(self, key, count):
        self.key = key
        self.count = count
        self.prev = None
        self.next = None


"""
    1st approach: hashtable + double link list
    - when we increment the count of a key, if the key.count >= tail.count, move it to the tail
    - when we decrement the count of a key, if the key.count <= tail.count, move it to the head

    1 corner case to to take care of:
    {
        a: 1
        b: 1
        c: 1
        d: 10
    }
    when we inc 'a', we need to move b or c to the head of the linked list
    
    Time of inc()           O(1) -> O(n)
    Time of dec()           O(1)
    Time of GetMaxKey()     O(1)
    Time of GetMinKey()     O(1)
    72 ms, faster than 88.41%
"""


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}
        self.listHead = ListNode(0, 0)
        self.listTail = ListNode(0, 0)
        self.listHead.next = self.listTail
        self.listTail.prev = self.listHead

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        if key not in self.m:
            node = ListNode(key, 1)
            self.m[key] = node
            # add to head
            head = self.listHead.next
            self.listHead.next = node
            node.prev = self.listHead
            node.next = head
            head.prev = node
        else:
            node = self.m[key]
            node.count += 1
            last = self.listTail.prev
            if node.key != last.key and node.count >= last.count:
                # unlink
                node.prev.next = node.next
                node.next.prev = node.prev
                # move to tail
                last.next = node
                node.prev = last
                node.next = self.listTail
                self.listTail.prev = node
                return
            for key in self.m:
                if self.m[key].count < node.count:
                    x = self.m[key]
                    # unlink
                    x.prev.next = x.next
                    x.next.prev = x.prev
                    # add to head
                    head = self.listHead.next
                    self.listHead.next = x
                    x.prev = self.listHead
                    x.next = head
                    head.prev = x
                    break

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if key not in self.m:
            return None
        node = self.m[key]
        node.count -= 1

        # print('dec1', node.key, node.count)

        if node.count == 0:
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.m[key]
            return
        head = self.listHead.next

        # print('dec2', head.key, head.count)

        if node.key != head.key and node.count <= head.count:
            # unlink
            node.prev.next = node.next
            node.next.prev = node.prev
            # add to head
            head = self.listHead.next
            self.listHead.next = node
            node.prev = self.listHead
            node.next = head
            head.prev = node

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        head = self.listHead.next
        # print("getMinKey", head.key, head.count)
        if head.count > 0:
            return head.key
        return ''

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        last = self.listTail.prev
        # print("getMaxKey", last.key, last.count)
        if last.count > 0:
            return last.key
        return ''


# helper
def printList(head):
    print("--printList start--")
    cur = head
    while cur != None:
        print(cur.key, cur.count)
        cur = cur.next
    print("--printList end--")


# case 11
obj = AllOne()
obj.inc('a')
obj.inc('b')
obj.inc('b')
obj.inc('c')
obj.inc('c')
obj.inc('c')
obj.dec('b')
obj.dec('b')
print(obj.getMinKey())
obj.dec('a')
print(obj.getMinKey())
print(obj.getMaxKey())

print("-----")

# case 15a
obj = AllOne()
obj.inc('hello')
obj.inc('world')
obj.inc('leet')
obj.inc('code')
obj.inc('DS')
obj.inc('leet')
print(obj.getMaxKey())
obj.inc('DS')
obj.dec('leet')
print(obj.getMaxKey())

print("-----")

# case15b
obj = AllOne()
obj.inc('a')
obj.inc('b')
obj.inc('c')
obj.inc('d')

obj.inc('a')
obj.inc('b')
obj.inc('c')
obj.inc('d')

obj.inc('c')
obj.inc('d')
obj.inc('d')
obj.inc('a')
# printList(obj.listHead)
print(obj.getMinKey())
print(obj.getMaxKey())
