from collections import *

"""
    1st approach: brute force hashset

    Time    O(SG)
    Space   O(G)
    984 ms, faster than 5.16%
"""


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bullsCount = 0
        cowsCount = 0
        i = 0
        while i < len(secret):
            a = secret[i]
            b = guess[i]
            if a == b:
                bullsCount += 1
                secret = secret[:i]+secret[i+1:]
                guess = guess[:i]+guess[i+1:]
            else:
                i += 1

        cowsSet = set()
        for i in range(len(secret)):
            for j in range(len(guess)):
                if secret[i] == guess[j]:
                    if j not in cowsSet:
                        cowsCount += 1
                        cowsSet.add(j)
                        break
        return str(bullsCount)+'A'+str(cowsCount)+'B'


a = "1807"
b = "7810"
print(Solution().getHint(a, b))

a = "1123"
b = "0111"
print(Solution().getHint(a, b))

print("-----")

"""
    2nd approach: hashtable
    1. remove the characters on the same indeces
    2. put the indeces to characters in guess
        e.g. 1213
        m = {
            1: [0, 2],
            2: [1],
            3: [2]
        }
    3. iterate through the guess and find if there is any character that we can match from the hashtable
        - if yes, remove an item from that array. it means that we found one and 'consume' that character in guess

    Time    O(2S+G)
    Space   O(G)
    40 ms, faster than 56.78%
"""


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bullsCount = 0
        cowsCount = 0
        i = 0
        while i < len(secret):
            a = secret[i]
            b = guess[i]
            if a == b:
                bullsCount += 1
                secret = secret[:i]+secret[i+1:]
                guess = guess[:i]+guess[i+1:]
            else:
                i += 1

        dfd = defaultdict(list)
        for i in range(len(guess)):
            c = guess[i]
            dfd[c].append(i)

        for c in secret:
            arr = dfd[c]
            if len(arr) > 0:
                cowsCount += 1
                arr.pop()

        return str(bullsCount)+'A'+str(cowsCount)+'B'


a = "1807"
b = "7810"
print(Solution().getHint(a, b))

a = "1123"
b = "0111"
print(Solution().getHint(a, b))
