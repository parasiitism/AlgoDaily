"""
    bit op
    - whenever we see continuous ones, we do n += 1, so that n will become xx00100..00
                                                                               ^     
    note:
    - to check continuous ones we use n&3, because 3&3 = 3, 7&3 = 3, 15&3 = 3, 31&3 = 3, .... 


    Time    O(logN)
    Space   O(1)
"""
class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n > 0:
            if n & 3 == 3:
                n += 1
                res += 1
            else:
                res += n & 1
                n >>= 1
        return res