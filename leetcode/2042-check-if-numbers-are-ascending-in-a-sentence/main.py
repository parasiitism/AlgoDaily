"""
    1st: string parsing
    
    Time    O(N)
    Space   O(N)
    32 ms, faster than 66.67%
"""


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split()
        prev = -1
        for w in words:
            if w.isdigit():
                if int(w) <= prev:
                    return False
                prev = int(w)
        return True
