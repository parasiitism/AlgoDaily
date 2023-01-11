from collections import Counter
from heapq import *


class HuffmanNode(object):
    def __init__(self, val=None, freq=0) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.freq = freq

    # comparator func for minheap https://stackoverflow.com/a/59956131/2090202
    def __lt__(self, other):
        return self.freq < other.freq


class Huffman:

    """
        In reality, the encoded outcome is in binary instead of str. 
        Here we just simulate how it works
    """
    @staticmethod
    def encode(s: str) -> HuffmanNode:
        minheap = []
        ctr = Counter(s)
        for c in ctr:
            freq = ctr[c]
            heappush(minheap, HuffmanNode(c, freq))
        while len(minheap) > 1:
            a = heappop(minheap)
            b = heappop(minheap)
            parent = HuffmanNode()
            parent.left = a
            parent.right = b
            parent.freq = a.freq + b.freq
            heappush(minheap, parent)
        root = heappop(minheap)

        def f(node, binaryStr):
            if node.val != None:
                return {node.val: binaryStr}
            d = dict()
            d.update(f(node.left, binaryStr + '0'))
            d.update(f(node.right, binaryStr + '1'))
            return d

        encoding_map = f(root, '')

        encoding_str = ''
        for c in s:
            encoding_str += encoding_map[c]

        return encoding_map, encoding_str

    @staticmethod
    def decode(encoding_map, encoding_str) -> str:

        binary_map = {}
        for key in encoding_map:
            binary_str = encoding_map[key]
            binary_map[binary_str] = key

        res = ''
        cur = ''
        for i in range(len(encoding_str)):
            c = encoding_str[i]
            cur += c
            if cur in binary_map:
                res += binary_map[cur]
                cur = ''
        return res


def _tests():
    cases = [
        "AABCBAD",
        "I am Calvin, from Hong Kong. Now I work at Facebook in London.",
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    ]
    for s in cases:
        encoding_map, encoding_str = Huffman.encode(s)
        t = Huffman.decode(encoding_map, encoding_str)
        print(s == t)


_tests()
