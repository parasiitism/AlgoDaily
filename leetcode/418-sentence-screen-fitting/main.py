"""
    1st: greedy?
    - basically we use an idx to indicate the start of each sentence
    - for each iteration
        - we advance the idx by number of columns, i.e. idx += cols
        - subtract idx until the last is a character
        - add a space after that last character
    - finally idx/len(s) is the result

    abc de f abc de f abc de f ...   // start=0
    012345                           // start=start+cols+adjustment=0+6+1=7 (1 space removed in screen string)
           012345                    // start=7+6+0=13
                 012345              // start=13+6-1=18 (1 space added)
                      012345         // start=18+6+1=25 (1 space added)
                             012345

    ref:
    - https://leetcode.com/problems/sentence-screen-fitting/discuss/90845/21ms-18-lines-Java-solution

    Time    O(N)
    Space   O(N)
    228 ms, faster than 40.50%
"""


class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = " ".join(sentence) + " "
        n = len(s)
        everyStartIdx = 0
        for _ in range(rows):
            # full fill current collumn, so everyStartIdx advance by cols
            everyStartIdx += cols
            # make sure s[everyStartIdx % s.length()] == ' '
            while everyStartIdx > 0 and s[everyStartIdx % n] != ' ':
                everyStartIdx -= 1
            # add a space at the end of the current repeating sentences
            everyStartIdx += 1
        # at the end, everyStartIdx should be the redundant space below the last row
        return everyStartIdx/n


print(Solution().wordsTyping(["hello"], 4, 4))
print(Solution().wordsTyping(["hell", "hello"], 4, 4))
print(Solution().wordsTyping(["hello"], 4, 5))
print(Solution().wordsTyping(["hello", "world"], 2, 8))
print(Solution().wordsTyping(["a", "bcd", "e"], 3, 6))
print(Solution().wordsTyping(["I", "had", "apple", "pie"], 4, 5))
print(Solution().wordsTyping(["try", "to", "be", "better"], 17, 2))
print(Solution().wordsTyping(["a", "b", "e"], 20000, 20000))
