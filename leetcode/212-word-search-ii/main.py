"""
    1st approach: naive approach
	- reuse the concept from lc79

	Time	O(k4^N)
	Space	O(4^N)
	TLE here in python
"""


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        wordSet = set(words)
        res = []
        for word in wordSet:
            if self.exist(board, word) == True:
                res.append(word)
        return res

    def exist(self, board, word):
        if len(board) == 0 or len(board[0]) == 0:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word, idx):
        # if all the characters are checked
        if len(word) == idx:
            return True
        # check boundaries
        if i < 0 or i+1 > len(board) or j < 0 or j+1 > len(board[0]):
            return False
        # if can go forward
        if word[idx] != board[i][j]:
            return False
        # first character is found, check the remaining part
        tmp = board[i][j]
        # avoid visit agian
        board[i][j] = "#"
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word, idx+1)\
            or self.dfs(board, i-1, j, word, idx+1)\
            or self.dfs(board, i, j+1, word, idx+1)\
            or self.dfs(board, i, j-1, word, idx+1)
        board[i][j] = tmp
        return res


"""
    2nd approach: trie + dfs
	- simlar logic with the concept from lc79

	Time	O(k4^N)
	Space	O(4^N)
	TLE here in python
"""


class Node(object):
    def __init__(self, isWord):
        self.children = 26*[None]
        self.isWord = isWord


class Trie(object):

    def __init__(self):
        self.root = Node(False)

    def insert(self, word):
        cur = self.root
        for w in word:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = Node(False)
            cur = cur.children[idx]
        cur.isWord = True

    def search(self, word):
        cur = self.root
        for w in word:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                return False
            cur = cur.children[idx]
        return cur.isWord


class Solution(object):

    def __init__(self):
        self.res = []

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(trie.root, board, i, j, "")
        return self.res

    # check whether can find word, start at (i,j) position
    def dfs(self, node, board, i, j, path):
        # if all the characters are checked
        if node.isWord:
            self.res.append(path)
            node.isWord = False
        # check boundaries
        if i < 0 or i+1 > len(board) or j < 0 or j+1 > len(board[0]):
            return
        # go on dfs with the trie
        temp = board[i][j]
        key = ord(temp)-ord('a')
        if key < 0 or key > 25 or node.children[key] == None:
            return
        node = node.children[key]
        # backtrack to avoid visit agian
        board[i][j] = "#"
        self.dfs(node, board, i+1, j, path+temp)
        self.dfs(node, board, i-1, j, path+temp)
        self.dfs(node, board, i, j+1, path+temp)
        self.dfs(node, board, i, j-1, path+temp)
        board[i][j] = temp
