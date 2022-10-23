"""
    strinig

    Time    O(1)
    Space   O(1)
    65 ms, faster than 33.33%
"""


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        a_s, a_e = self.time2min(event1[0]), self.time2min(event1[1])
        b_s, b_e = self.time2min(event2[0]), self.time2min(event2[1])
        if a_s > b_s:
            a_s, a_e, b_s, b_e = b_s, b_e, a_s, a_e
        if a_e >= b_s:
            return True
        return False

    def time2min(self, event):
        hh = int(event[:2])
        mm = int(event[3:])
        return hh*60 + mm
