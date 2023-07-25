"""
    brute-force

    Time    O(M+A)
    Space   O(1)
"""


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        res = 0
        used = 0
        while mainTank > 0:
            mainTank -= 1
            used += 1
            res += 10
            if used % 5 == 0 and additionalTank >= 1:
                mainTank += 1
                additionalTank -= 1
        return res
