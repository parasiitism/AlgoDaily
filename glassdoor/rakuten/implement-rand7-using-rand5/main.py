import sys

# The rand5() API is already defined for you.
# def rand5():
# @return a random integer in the range 1 to 5

"""
    1st approach: learned from others

    Rejection Sampling
        1   2   3   4   5   <- rand5()
    1   1   2   3   4   5
    2   6   7|  8   9  10
    3   11  12  13 14| 15
    4   16  17  18  19 20
    5   21| 22  23  24 25 
    ^
    rand5()

    - the numbers are equally distributed from 0 to 20
    - but from 21 to 24, the distribution doesn't equal(because there are no 25, 26, 27), so rand() again

    ref:
    - https://www.youtube.com/watch?v=Wyauxe92JJA

    Time    O(1) average but O(inf) if unlucky
    Space   O(1)
"""

import random


def rand5():
    # one-based random
    return random.randint(1, 4)


class Solution(object):
    def rand7(self):
        num = sys.maxsize
        while num > 21:
            row = rand5()
            col = rand5()
            num = (row-1) * 5 + col
        return num % 7 + 1


print(Solution().rand7())
print(Solution().rand7())
print(Solution().rand7())
print(Solution().rand7())
print(Solution().rand7())
print(Solution().rand7())
print(Solution().rand7())
