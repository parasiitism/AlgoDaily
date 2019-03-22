class Node(object):
    def __init__(self, children, is_word):
        self.children = children
        self.is_word = is_word


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node({}, False)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = Node({}, False)
            cur = cur.children[w]
        cur.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return cur.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for w in prefix:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return True


obj = Trie()
obj.insert('abc')
print(obj.root.children)
print(obj.search('abc'))
print(obj.startsWith('a'))

print("-----")


class Node(object):
    def __init__(self, is_word):
        self.children = 26*[None]
        self.is_word = is_word


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
        cur.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for w in word:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                return False
            cur = cur.children[idx]
        return cur.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for w in prefix:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                return False
            cur = cur.children[idx]
        return True


obj = Trie()
obj.insert('abc')
print(obj.root.children)
print(obj.search('abc'))
print(obj.startsWith('a'))
