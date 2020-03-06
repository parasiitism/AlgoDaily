from typing import List

"""
    1st: trie
    - put all the reversed words into a trie
    - the shortest string can be formed by all the leaf nodes

    Time    O(MN)
    Space   O(MN)
    1452 ms, faster than 5.03%
"""


class Node(object):
    def __init__(self, is_word: bool) -> None:
        self.children = 26*[None]
        self.is_word = is_word


class Trie(object):

    def __init__(self):
        self.root = Node(False)

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = Node(False)
            cur = cur.children[idx]
        cur.is_word = True


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # put all the reversed words into a trie
        t = Trie()
        for w in words:
            t.insert(w[::-1])

        res = 0
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        # DFS to find out all the leaves

        def dfs(node, path):
            nonlocal res
            if node == None:
                return

            isLeaf = True
            for i in range(len(node.children)):
                child = node.children[i]
                dfs(child, path + alphabet[i])
                if child != None:
                    isLeaf = False

            if node.is_word and isLeaf:
                res += 1 + len(path)

        dfs(t.root, "")
        return res
