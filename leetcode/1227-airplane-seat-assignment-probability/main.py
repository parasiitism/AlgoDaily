"""
    1st: brain teaser
    - this is not a good interview question
    - i just ran the editor and saw that f(N) = 0.5 for N >= 2, so submitted it

    math explanation:
    - https://leetcode.com/problems/airplane-seat-assignment-probability/discuss/669454/Python-Simple-DP-solution-with-explanation

    Time    O(1)
    Space   O(1)
    41 ms, faster than 27.55%
"""


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        return 0.5
