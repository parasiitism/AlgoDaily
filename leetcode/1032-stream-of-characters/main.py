from collections import defaultdict

"""
    1st: trie, better brute force
    - init(words):
        - put all the words into a trie
        - declare a list for us to store the potential candidates, in terms of references
    - query(letter):
        - try to see if we can extend from the candidates list
        - put the one character into the candidates list if its valid (on which some words start with)
    
    Time of __init__()      O(W)
    Space of query()        O(N)
    9812 ms, faster than 5.33%
"""


class Node(object):
    def __init__(self, is_word):
        self.children = 26*[None]
        self.is_word = is_word


class Trie(object):

    def __init__(self):
        self.root = Node(False)

    def insert(self, word):
        cur = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = Node(False)
            cur = cur.children[idx]
        cur.is_word = True


class StreamChecker(object):

    def __init__(self, words):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        self.cands = []  # candidates

    def query(self, letter):
        idx = ord(letter) - ord('a')
        newCands = []
        isFound = False
        for cand in self.cands:
            if cand.children[idx] != None:
                newCands.append(cand.children[idx])
                if cand.children[idx].is_word:
                    isFound = True
        if self.trie.root.children[idx] != None:
            newCands.append(self.trie.root.children[idx])
            if self.trie.root.children[idx].is_word:
                isFound = True

        self.cands = newCands
        return isFound


"""
    2nd: hashtable
    - init(words): put the words into a hashtable with the last character as key
        e.g, words = [a, bc, def, ok, lok, ook]
        hashtable = {
            a: a,
            c: bc,
            f: def,
            k: ok, lok, ook
        }
    - query(letter): for each set of key(letter), i.e, hashtabe[letter], check if the aggregated string exists
        e.g. abcdfgdlo[k]   <- k is the latest query
        hashtable[k] = {ok, lok, ook}
        Since aggregated string ends with ok, lok, return True
"""


class StreamChecker:

    def __init__(self, words):
        self.s = ''
        self.ht = defaultdict(set)
        for w in words:
            self.ht[w[-1]].add(w)

    def query(self, letter):
        self.s += letter
        # approach 1: 4 lines
        res = False
        for w in self.ht[letter]:
            res = res or self.s.endswith(w)
        return res
        # approach 2: Or 1 line
        # return any(self.s.endswith(w) for w in self.dic[letter])
