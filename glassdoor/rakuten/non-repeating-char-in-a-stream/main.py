class DLLNode(object):
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


class Solution(object):
    def __init__(self):
        self.m = {}
        self.head = DLLNode("#")
        self.tail = DLLNode("#")
        self.head.next = self.tail
        self.tail.prev = self.head

    def streamAdd(self, c):
        if c not in self.m:
            # add to the queue
            node = DLLNode(c)
            self.m[c] = node
            # add to tail
            last = self.tail.prev
            last.next = node
            node.prev = last
            node.next = self.tail
            self.tail.prev = node
        else:
            # remove node from queue
            node = self.m[c]
            if node.prev != None:
                node.prev.next = node.next
            if node.next != None:
                node.next.prev = node.prev
            node.prev = None
            node.next = None
        # first node is the first non-repeating char
        first = self.head.next
        if first == self.tail:
            return None
        return first.key


s = Solution()
print(s.streamAdd('l'))
print(s.streamAdd('o'))
print(s.streamAdd('v'))
print(s.streamAdd('e'))
print(s.streamAdd('l'))
print(s.streamAdd('e'))
print(s.streamAdd('e'))
print(s.streamAdd('t'))
print(s.streamAdd('c'))
print(s.streamAdd('o'))
print(s.streamAdd('d'))
print(s.streamAdd('e'))
print(s.streamAdd('v'))

print("-----")

s = Solution()
print(s.streamAdd('l'))
print(s.streamAdd('o'))
print(s.streamAdd('v'))
print(s.streamAdd('e'))
print(s.streamAdd('l'))
print(s.streamAdd('e'))
# print(s.streamAdd('e'))
print(s.streamAdd('t'))
print(s.streamAdd('v'))

print("-----")
s = Solution()
print(s.streamAdd('a'))
print(s.streamAdd('b'))
print(s.streamAdd('c'))
print(s.streamAdd('c'))
print(s.streamAdd('b'))
print(s.streamAdd('a'))
print(s.streamAdd('d'))
