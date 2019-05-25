"""
    learned from others
    - u will lost when n=4,8,12,16,…, basically all multiples of 4

    ref:
    - https://leetcode.com/problems/nim-game/solution/
    - https://www.youtube.com/watch?v=dUXW3Kh_kxo
"""


class Solution(object):
    def canWinNim(self, n):
        return n % 4 != 0
