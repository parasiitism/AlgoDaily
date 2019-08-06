"""
    1st approach: sort
    - construct the result from the back

    e.g.

                                                    result = [2,13,3,11,5,17,7]
    We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
    We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
    We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
    We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
    We reveal 11, and move 17 to the bottom. The deck is now [13,17].
    We reveal 13, and move 17 to the bottom. The deck is now [17].
    We reveal 17.
    
    Time    O(nlogn), it wont take O(n^2) because when we do arr.insert(k), k = 1 in our case
    Space   O(n)
    52 ms, faster than 25.64%
"""


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        clone = sorted(deck)
        res = []
        while len(clone) > 0:
            res = [clone.pop()] + res
            if len(res) > 1:
                res.insert(1, res.pop())
        return res
