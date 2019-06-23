# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

"""
    1st approach: learned from others

    Rejection Sampling
        1   2   3   4   5   6   7   <- rand7()
    1   1   2   3   4   5   6   7
    2   8   9   10| 11  12  13  14
    3   15  16  17  18  19  20| 21
    4   22  23  24  25  26  27  28
    5   29  30| 31  32  33  34  35
    6   36  37  38  39  40| 41  42
    7   43  44  45  46  47  48  49
    ^
    rand7()

    - the numbers are equally distributed from 0 to 39
    - but from 40 to 48, the distribution doesn't equal(because there is no 49), so rand() again

    ref:
    - https://www.youtube.com/watch?v=Wyauxe92JJA

    Time    O(1) average but O(inf) if unlucky
    Space   O(1)
    384ms beats 92%
"""

import random


def rand7():
    # one-based random
    return random.randint(1, 7)


class Solution(object):
    def rand10(self):
        num = sys.maxsize
        while num > 40:
            row = rand7()
            col = rand7()
            num = (row-1) * 7 + col
        return num % 10 + 1


print(Solution().rand10())
print(Solution().rand10())
print(Solution().rand10())
print(Solution().rand10())
print(Solution().rand10())
print(Solution().rand10())
print(Solution().rand10())
print(Solution().rand10())
print(Solution().rand10())
print(Solution().rand10())
