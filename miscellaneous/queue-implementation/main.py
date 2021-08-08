"""
    To implement an queue efficiently, we should use a Doubly Linked List
    So then, all the operations would be in O(1)
"""


class LLNode(object):
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None


class Queue(object):
    def __init__(self):
        self.count = 0
        self.head = LLNode()
        self.tail = LLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def enqueue(self, val):
        node = LLNode(val)
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node
        self.count += 1
        return None

    def dequeue(self):
        if self.isEmpty():
            return None
        first = self.head.next
        self.head.next = first.next
        first.next.prev = self.head
        self.count -= 1
        return first.val

    def peek(self):
        if self.isEmpty():
            return None
        return self.head.next.val

    def isEmpty(self):
        return self.head.next == self.tail

    def getLength(self):
        return self.count


def checkQueue(q):
    res = []
    cur = q.head
    while cur != None:
        res.append(cur.val)
        cur = cur.next
    print('the queue=', res)
    print('peek=', q.peek())
    print('isEmpty=', q.isEmpty())
    print('getLength=', q.getLength())


q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
checkQueue(q)
print('dequeue', q.dequeue())
q.enqueue(4)
checkQueue(q)
print('dequeue', q.dequeue())
print('dequeue', q.dequeue())
print('dequeue', q.dequeue())
print('dequeue', q.dequeue())
checkQueue(q)
