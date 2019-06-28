"""
    1st approach: hashtable

    Time of buildDict()     O(n)
    Time of search()        O(26k) k: length of the input word
    Space                   O(n)
    24 ms, faster than 50.12%
"""


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = set()

    def buildDict(self, dic):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for w in dic:
            self.m.add(w)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(word)):
            curIdx = ord(word[i]) - ord('a')
            for j in range(26):
                if j != curIdx:
                    temp = word[:i] + alphabets[j] + word[i+1:]
                    if temp in self.m:
                        return True
        return False


"""
    2nd approach: trie

    Time of buildDict()     O(nk)
    Time of search()        O(26kk)
    Space                   O(n)
    80 ms, faster than 5.19%
"""


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def buildDict(self, dic):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for w in dic:
            self.trie.insert(w)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(word)):
            curIdx = ord(word[i]) - ord('a')
            for j in range(26):
                if j != curIdx:
                    temp = word[:i] + alphabets[j] + word[i+1:]
                    if self.trie.search(temp):
                        return True
        return False


class Node(object):
    def __init__(self, is_word):
        self.children = 26*[None]
        self.is_word = is_word


class Trie(object):

    def __init__(self):
        self.root = Node(False)

    def insert(self, word):
        cur = self.root
        for c in word:
            idx = ord(c)-ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = Node(False)
            cur = cur.children[idx]
        cur.is_word = True

    def search(self, word):
        cur = self.root
        for c in word:
            idx = ord(c)-ord('a')
            if cur.children[idx] == None:
                return False
            cur = cur.children[idx]
        return cur.is_word
