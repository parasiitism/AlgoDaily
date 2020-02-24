from typing import List

"""
    1st: math

    Time    O(N)
    Space   O(N)
    60 ms, faster than 70.88%
"""


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        m = None
        for i in range(1, len(coordinates)):
            prev = coordinates[i-1]
            curr = coordinates[i]
            m_ = None
            if curr[0] - prev[0] == 0:
                m_ = 'inf'
            else:
                m_ = (curr[1] - prev[1]) / (curr[0] - prev[0])
            if i == 1:
                m = m_
            else:
                if m != m_:
                    return False
        return True
