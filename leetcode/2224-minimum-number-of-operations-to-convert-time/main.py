"""
    1st: math

    Time    O(N)
    Space   O(N)
    36 ms, faster than 79.89%
"""


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        A = self.getTotalMins(current)
        B = self.getTotalMins(correct)

        m60, m15, m5, m1 = 0, 0, 0, 0

        if B - 60 >= A:
            m60, B = (B - A) // 60, (B - A) % 60 + A

        if B - 15 >= A:
            m15, B = (B - A) // 15, (B - A) % 15 + A

        if B - 5 >= A:
            m5, B = (B - A) // 5, (B - A) % 5 + A

        if B > A:
            m1 = B - A

        return m60 + m15 + m5 + m1

    def getTotalMins(self, T):
        hh = int(T[:2])
        mm = int(T[3:])
        return hh*60 + mm
