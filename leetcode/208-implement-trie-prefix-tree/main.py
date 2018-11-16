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
        for i in range(len(word)):
            w = word[i]
            temp = None
            if w in cur.children:
                temp = cur.children[w]
            else:
                temp = Node({}, False)
            if i == len(word) - 1:
                temp.is_word = True
            cur.children[w] = temp
            cur = temp

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for i in range(len(word)):
            w = word[i]
            if w in cur.children:
                cur = cur.children[w]
                if i == len(word) - 1 and cur.is_word:
                    return True
            else:
                return False
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for i in range(len(prefix)):
            w = prefix[i]
            if w in cur.children:
                cur = cur.children[w]
                if i == len(prefix) - 1:
                    return True
            else:
                return False
        return False


obj = Trie()
obj.insert('abc')
print(obj.root.children)
print(obj.search('abc'))
print(obj.startsWith('a'))
