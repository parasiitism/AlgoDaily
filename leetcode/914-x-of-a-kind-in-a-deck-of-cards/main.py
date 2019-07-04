"""
    1st approach: GCD
    - count occurence of each number
    - find the GCD of the occurence
    - if GCD >= 2, return true

    Time    O(nlogn) -> O(n^2) suggerted solution says it takes O(N*(logN)^2) but i dont understand
    Space   O(n)
    116 ms, faster than 98.70% 
"""


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck) == 0:
            return False
        m = {}
        for x in deck:
            if x not in m:
                m[x] = 1
            else:
                m[x] += 1
        cards = []
        for key in m:
            cards.append(m[key])
        gcd = cards[0]
        for i in range(1, len(cards)):
            gcd = self.gcd(gcd, cards[i])
        return gcd >= 2

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
