class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        1st approach: similar to leetcode217) word ladder
        BFS + hashset to avoid loop for each path

        LTE
        """
        wordList = set(wordList)  # avoid duplicate words
        # BFS
        q = []
        q.append((beginWord, [beginWord], set()))
        # seen = set()  # avoid revisting a seen word
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        temps = []
        shortest = len(wordList)
        while len(q) > 0:
            word, path, seen = q.pop(0)
            if word == endWord:
                if len(path) < shortest:
                    shortest = len(path)
                temps.append(path)
            if len(path) > len(wordList):
                break
            # explore at index=0 hit => ait, bit, cit....
            # explore at index=1 hit => hat, hbt, hct....
            for i in range(len(word)):
                for c in alphabets:
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordList and newWord not in seen:
                        newSet = set(seen)
                        newSet.add(newWord)
                        q.append((newWord, path + [newWord], newSet))
                        seen.add(newWord)
        res = []
        for temp in temps:
            if len(temp) == shortest:
                res.append(temp)
        return res


a = "abc"
b = "ade"
c = ["abd", "azd", "add", "ade"]
print(Solution().findLadders(a, b, c))

a = "hit"
b = "cog"
c = ["hot", "dot", "dog", "lot", "log", "cog"]
print(Solution().findLadders(a, b, c))

a = "hit"
b = "cog"
c = ["hot", "dot", "dog", "lot", "log"]
print(Solution().findLadders(a, b, c))

a = "leet"
b = "code"
c = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
print(Solution().findLadders(a, b, c))

a = "qa"
b = "sq"
c = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
print(Solution().findLadders(a, b, c))
