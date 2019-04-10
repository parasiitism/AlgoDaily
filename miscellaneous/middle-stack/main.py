class DLLNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MiddleStack(object):

    def __init__(self):
        self.head = DLLNode(0)
        self.tail = DLLNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.middle = self.head
        self.count = 0

    def push(self, x):
        last = self.tail.prev
        node = DLLNode(x)
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

        # when it is an odd, move forward
        self.count += 1
        if self.count % 2 == 1:
            self.middle = self.middle.next

    def pop(self):
        last = self.tail.prev
        last.prev.next = last.next
        last.next.prev = last.prev

        # when it is an even, move backward
        self.count -= 1
        if self.count % 2 == 0:
            self.middle = self.middle.prev
        return last.val

    def top(self):
        return self.tail.prev.val

    def peekMiddle(self):
        return self.middle.val

    def popMiddle(self):
        m = self.middle.val
        self.middle.prev.next = self.middle.next
        self.middle.next.prev = self.middle.prev
        # very tricky here
        self.count -= 1
        if self.count % 2 == 0:
            # this part is the same with pop(0)
            self.middle = self.middle.prev
        else:
            self.middle = self.middle.next

        return m


ms = MaxStack()
ms.push(1)
ms.push(2)
ms.push(3)
ms.push(4)
print(ms.top())  # 4
print(ms.pop())  # 4
print(ms.peekMiddle())  # 2
print(ms.popMiddle())  # 2
print(ms.peekMiddle())  # 1
print(ms.top())  # 3
ms.push(5)
print(ms.peekMiddle())  # 3

print("-----")

ms = MaxStack()
ms.push(1)
print(ms.peekMiddle())  # 1
print(ms.popMiddle())  # 1
ms.push(2)
ms.push(3)
ms.push(4)
print(ms.top())  # 4
print(ms.pop())  # 4
print(ms.peekMiddle())  # 2
print(ms.popMiddle())  # 2
print(ms.top())  # 3
ms.push(5)
print(ms.peekMiddle())  # 3
