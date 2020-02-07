"""
    1st: trie
    - this is a very memory consuming approach
    - every node stores a whole list of words that starts with that prefix

    Time    O(NlogN)   <- logN if the trie is balence
    Space   O(N^2)     <- every node store N words 
    492 ms, faster than 23.21%
"""


class Node(object):
    def __init__(self, is_word):
        self.children = 26*[None]
        # self.is_word = is_word
        self.arr = []


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(False)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for w in word:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = Node(False)
            cur = cur.children[idx]
            cur.arr.append(word)

    def startsWith(self, prefix):
        """
        followup: print all the words startwith prefix
        :type prefix: str
        :rtype: []
        """
        cur = self.root
        for w in prefix:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                return []
            cur = cur.children[idx]
        return cur.arr


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        trie = Trie()

        for p in products:
            trie.insert(p)

        res = []
        prefix = ''
        for c in searchWord:
            prefix += c
            temp = trie.startsWith(prefix)
            temp.sort()
            res.append(temp[:3])
        return res
