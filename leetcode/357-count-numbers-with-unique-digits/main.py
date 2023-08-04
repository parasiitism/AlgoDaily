"""
    1st approach: math

    - For the first (most left) digit, we have 9 options (no zero); 
    - For the second digit we used one but we can use 0 now, so 9 options; 
    - and we have 1 less option for each following digits. 
    - Number can not be longer than 10 digits.    

    Time  O(n)
    Space O(1)
    20 ms, faster than 66.67% 
"""


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        total, start = 10, 9
        for i in range(1, n):
            start = start*(10-i)
            total += start
        return total
