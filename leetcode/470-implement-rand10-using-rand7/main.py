# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

"""
    1st approach: learned from others

    Rejection Sampling
        1   2   3   4   5   6   7   <- rand7()
    1   0   1   2   3   4   5   6
    2   7   8   9|  10  11  12  13
    3   14  15  16  17  18  19| 20
    4   21  22  23  24  25  26  27
    5   28  29| 30  31  32  33  34
    6   35  36  37  38  39| 40  41
    7   42  43  44  45  46  47  48
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


class Solution(object):
    def rand10(self):
        index = 100
        while index >= 40:
            index = (rand7()-1) * 7 + (rand7() - 1)
        return index % 10 + 1
