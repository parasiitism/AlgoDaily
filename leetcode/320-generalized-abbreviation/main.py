"""
    1st approach: recursion similar to subset
    - in each recursion, the base case is there is no more alphabet character we can continue
    - for each character, start the count with one. add up the number in front of it and the number behind it
    
    corner case:
    e.g.
    
    ab13c
     ^
     i

    The result should be a14c but not a23c

    Time    O(n2^n) <= O(2^n): each character has 2 options(number OR to stay). O(n): find the prefix and suffix number in each iteration
    Space   O(2^n)
    900 ms, faster than 5.35%
"""


class Solution(object):

    def __init__(self):
        self.res = []
        self.seen = set()

    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        self.recur(word)
        return self.res

    def recur(self, word):
        # avoid redundant calculation
        if word in self.seen:
            return
        self.seen.add(word)
        # similar to subset, we need to record all paths
        self.res.append(word)
        # the base case is there is no more alphabet character we can continue
        for i in range(len(word)):
            c = word[i]
            if c.isdigit() == False:
                count = 1
                # get the multi-digited number in front of this character
                j = i
                while j-1 >= 0 and word[j-1].isdigit():
                    j -= 1
                if len(word[j:i]) > 0:
                    count += int(word[j:i])
                prefix = word[:j]
                # get the multi-digited number behind this character
                j = i
                while j+1 < len(word) and word[j+1].isdigit():
                    j += 1
                if len(word[i+1:j+1]) > 0:
                    count += int(word[i+1:j+1])
                suffix = word[j+1:]
                # put the prefix, count and suffix together for the next recursion
                temp = prefix + str(count) + suffix
                self.recur(temp)


print(Solution().generateAbbreviations(""))
print(Solution().generateAbbreviations("a"))
print(Solution().generateAbbreviations("word"))
print(Solution().generateAbbreviations("calvin"))
# 2048
print(len(Solution().generateAbbreviations("interaction")))


print("-----")

"""
    2nd approach: recursion similar to 1st
    - BUT here we used # represent the count so that we dont have to deal with the corner cases like b13 -> 14

    Time    O(n2^n) <= O(2^n) each character has 2 options(number OR to stay). O(n) transform a###b##c# to a3b2c1
    Space   O(2^n)
    924 ms, faster than 5.35%
"""


class Solution(object):

    def __init__(self):
        self.res = []
        self.seen = set()

    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        self.recur(word)
        return self.res

    def recur(self, word):
        # avoid redundant calculation
        if word in self.seen:
            return
        self.seen.add(word)
        # similar to subset, we need to record all paths
        self.res.append(self.transform(word))
        # the base case is there is no more alphabet character we can continue
        for i in range(len(word)):
            c = word[i]
            if c.isdigit() == False:
                temp = word[:i] + '#' + word[i+1:]
                self.recur(temp)

    def transform(self, s):
        """
        e.g. a###b##c# -> a3b2c1
        """
        count = 0
        res = ""
        for c in s:
            if c == '#':
                count += 1
            else:
                if count > 0:
                    res += str(count)
                    count = 0
                res += c
        if count > 0:
            res += str(count)
        return res


print(Solution().generateAbbreviations(""))
print(Solution().generateAbbreviations("a"))
print(Solution().generateAbbreviations("word"))
print(Solution().generateAbbreviations("calvin"))
# 2048
print(len(Solution().generateAbbreviations("interaction")))


print("-----")
