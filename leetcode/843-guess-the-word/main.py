# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

import random

"""
    1st approach: array slicing + random
    - the question mentions that you can at most guess 10 times
    - the intuitive way is to narrow down the list by finding the words that have the same guessCount
    
    Time    O(10mn)
    Space   O(n)
    12 ms, faster than 97.62%
"""


class Solution(object):

    def __init__(self):
        self.arr = []

    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        self.arr = wordlist[:]
        for _ in range(10):
            ridx = random.randint(0, len(self.arr)-1)
            target = self.arr[ridx]
            count = master.guess(target)
            if count == -1:
                continue
            self.shrinkList(target, count)

    def shrinkList(self, guess, guessCount):
        temp = []
        for x in self.arr:
            if guessCount == self.match(guess, x):
                temp.append(x)
        self.arr = temp

    def match(self, guess, x):
        count = 0
        for i in range(len(x)):
            if x[i] == guess[i]:
                count += 1
        return count
