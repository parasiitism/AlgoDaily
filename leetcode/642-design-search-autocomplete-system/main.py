import operator


class Trie(object):
    def __init__(self, children, is_word, count):
        self.children = children
        self.is_word = is_word
        self.count = count


class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.history = ''
        self.trie = Trie({}, False, 0)
        for i in range(len(sentences)):
            self._insert(sentences[i], times[i])

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            self._insert(self.history, 0)
            self.history = ''
            return []
        else:
            self.history += c
            return self._search()

    def _insert(self, sentence, count):
        cur = self.trie
        for i in range(len(sentence)):
            w = sentence[i]
            temp = None
            if w in cur.children:
                temp = cur.children[w]
            else:
                temp = Trie({}, False, 0)
            if i == len(sentence) - 1:
                temp.is_word = True
                if count == 0:
                    temp.count += 1
                else:
                    temp.count = count
            cur.children[w] = temp
            cur = temp

    def _search(self):
        """
        1. search node in a trie
        2. dfs
        3. sort
        """
        # search
        prefix = self.history
        target = self.trie
        for w in prefix:
            if w not in target.children:
                return []
            target = target.children[w]
        leafs = []

        # dfs
        def dfs(node, route):
            if node.is_word:
                # trick: use negative count and enjoy the simple python sort
                leafs.append((-node.count, prefix+route))
            for key in node.children:
                dfs(node.children[key], route+key)
        dfs(target, "")
        leafs = sorted(leafs)

        # sort
        return [x[1] for x in leafs[:3]]


sentences = ['i love you', 'island', 'ironman', 'i love leetcode', 'ia']
times = [5, 3, 2, 2, 2]
obj = AutocompleteSystem(sentences, times)
print(obj.input('i'))
print(obj.input(' '))
# obj.input('a')
# obj.input('#')
