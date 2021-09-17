"""
    1st: Sprague–Grundy theorem and the Colon Principle
    - it is not a good interview question

    Time    O(1)
    Space   O(1)
"""


class Solution:
    def findGameWinner(self, n: int) -> bool:
        return n % 6 != 1
