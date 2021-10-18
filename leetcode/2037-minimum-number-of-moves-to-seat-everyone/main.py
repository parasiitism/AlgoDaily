"""
    1st: sort
    
    1   4   5   9
    1   2   3   6
    --------------
    0   +2  +1  +3
    
    2   2   6   6
    1   2   3   6
    -------------
    +1  0   +3  0

    Time    O(NlogN)
    Space   O(1)
    64 ms, faster than 70.00%
"""


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        seats.sort()
        students.sort()
        res = 0
        for i in range(n):
            res += abs(seats[i] - students[i])
        return res
