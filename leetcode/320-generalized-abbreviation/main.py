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

    Time    O(2^n)
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
