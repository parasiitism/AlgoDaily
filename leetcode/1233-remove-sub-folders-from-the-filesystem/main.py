"""
    1st: trie + dfs

    Time    O(NM)
    Space   O(N)
    468 ms, faster than 15.78%
"""


class Node(object):
    def __init__(self, children, is_word):
        self.children = children
        self.is_word = is_word


class Trie(object):

    def __init__(self):
        self.root = Node({}, False)

    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = Node({}, False)
            cur = cur.children[w]
        cur.is_word = True

    def findRoots(self):
        res = []

        def dfs(node, path):
            if node == None:
                return
            if node.is_word:
                res.append(path)
                return
            for key in node.children:
                child = node.children[key]
                dfs(child, path + '/' + key)
        dfs(self.root, "")
        return res


class Solution:
    def removeSubfolders(self, folders):
        folders = [f.split('/')[1:] for f in folders]
        trie = Trie()
        for f in folders:
            trie.insert(f)
        return trie.findRoots()


s = Solution()

a = ["/a", "/a/b/c", "/a/b/d"]
print(s.removeSubfolders(a))

a = ["/a/b", "/c/d/e", "/c/f", "/a", "/c/d", "/a/b/d", "/a/b/ca", "/a/b/c"]
print(s.removeSubfolders(a))

print("-----")


"""
    2nd: 
    1. sort folder by length
    2. check if the floder's parent fold in a hashset before adding it into the hashset

    Time    O(NlogN + NM)
    Space   O(N)
    296 ms, faster than 54.50%
"""


class Solution(object):
    def removeSubfolders(self, folders):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folders.sort(key=len)
        seen = set()
        for f in folders:
            isRoot = True
            for i in range(2, len(f)):
                if f[i] == '/' and f[: i] in seen:
                    isRoot = False
                    break
            if isRoot:
                seen.add(f)
        return list(seen)
