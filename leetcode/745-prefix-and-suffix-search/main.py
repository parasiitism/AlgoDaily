"""
    1st approach: trie

    Time of insert()        O(nk)
    Time if startsWith()    O(nk^2)
    LTE
"""


class Node(object):
    def __init__(self, isWord):
        self.children = 26*[None]
        self.isWord = isWord
        self.weight = -1


class Trie(object):

    def __init__(self):
        self.root = Node(False)

    def insert(self, word, weight):
        cur = self.root
        for w in word:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = Node(False)
            cur = cur.children[idx]
        cur.isWord = True
        cur.weight = weight

    def startsWith(self, prefix, suffix):
        cur = self.root
        for w in prefix:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                return -1
            cur = cur.children[idx]

        maxWeight = -1
        res = ""

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        def dfs(node, path):
            nonlocal maxWeight
            nonlocal res
            if node == None:
                return
            if node.isWord:
                temp = prefix+path
                if temp[len(temp)-len(suffix):] == suffix and node.weight > maxWeight:
                    maxWeight = node.weight
                    res = temp
            for i in range(len(node.children)):
                child = node.children[i]
                dfs(child, path + alphabet[i])

        dfs(cur, "")
        return maxWeight


class WordFilter(object):

    def __init__(self, words):
        self.trie = Trie()
        for i in range(len(words)):
            self.trie.insert(words[i], i)

    def f(self, prefix, suffix):
        return self.trie.startsWith(prefix, suffix)


"""
    2nd approach: hashtable
    - build all combinations of prefix + '#' +suffix for each word and put them into a hashtable
    - hashtable look up

    hints: For each test case, up to words.length queries WordFilter.f may be made.
    it means that there will be so many calls on f(), so we need to optimize the time of each f()

    e.g. 'ape'
    {
        '#ape': 0, 
        '#pe': 0, 
        '#e': 0, 
        '#': 0, 
        'a#ape': 0, 
        'a#pe': 0, 
        'a#e': 0, 
        'a#': 0, 
        'ap#ape': 0, 
        'ap#pe': 0, 
        'ap#e': 0, 
        'ap#': 0, 
        'ape#ape': 0, 
        'ape#pe': 0, 
        'ape#e': 0, 
        'ape#': 0,
    }

    ref:
    - https://leetcode.com/problems/prefix-and-suffix-search/discuss/110053/Python-few-ways-to-do-it-with-EXPLANATIONS!-U0001f389

    Time of init()      O(nkk)
    Time of f()         O(1)
    420 ms, faster than 71.43% 
"""


class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.m = {}
        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)+1):
                for k in range(len(word)+1):
                    temp = word[:j] + '#' + word[k:]
                    self.m[temp] = i

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        key = prefix + '#' + suffix
        if key in self.m:
            return self.m[key]
        return -1
