"""
    1st: just count

    Time    O(N)
    Space   O(1)
    112 ms, faster than 98.46%
"""


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fives = 0
        tens = 0
        for bill in bills:
            target = bill - 5
            # subtract 10 dollar
            if target >= 10 and tens > 0:
                tens -= 1
                target -= 10
            # subtract a number of 5 dollars
            count = target/5
            if fives >= count:
                fives -= count
            else:
                return False
            # increment count of 5 or 10 dollar
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
        return True
