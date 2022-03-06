"""
    1st: trie
    - the hardest way

    Time    O(N+logN)
    Space   O(N)
    228 ms, faster than 5.20%
"""


class Node(object):
    def __init__(self, cnt=0):
        self.children = 26*[None]
        self.cnt = cnt


class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for c in word:
            idx = ord(c)-ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = Node()
            cur = cur.children[idx]
        cur.cnt += 1

    def countStartsWith(self, prefix):
        cur = self.root
        for w in prefix:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                return 0
            cur = cur.children[idx]
        cnt = 0
        q = [cur]
        while len(q) > 0:
            node = q.pop(0)
            cnt += node.cnt
            for child in node.children:
                if child != None:
                    q.append(child)
        return cnt


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for w in words:
            trie.insert(w)
        return trie.countStartsWith(pref)


"""
    2nd: string

    Time    O(N)
"""


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for w in words:
            if w.startswith(pref):
                res += 1
        return res


"""
    3rd: one-line

    Time    O(N)
"""


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(w.startswith(pref) for w in words)


"""
    follow-up:
    - What if the words are sorted alphabetically already?
        - binary search
"""
