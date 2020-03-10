from typing import List
from collections import Counter

"""
    1st: 2 hashtables
    - 1 hashtable for counter
    - 1 hashtable for saving the tails of each chains
    - at each index:
        - try to chain up with any one of the chains that we came up with
        - else, chain up 3 items starting from itself

    e.g. [1, 2, 3, 3, 4, 4, 5, 5]
    
    At the beginning:
    counter = {
        1: 1,
        2: 1,
        3: 2,
        4: 2,
        5: 2,
    }
    tails = {}

    At index = 0: start another chain from "1" -> chain up "1,2,3"
    counter = {
        1: 0,
        2: 0,
        3: 1,
        4: 2,
        5: 2,
    }
    tails = {
        4: 1,
    }

    At index = 1, do nothing becos we used up "2"

    At index = 2, start another chain from "3" -> "3,4,5"
    counter = {
        1: 0,
        2: 0,
        3: 0,
        4: 1,
        5: 1,
    }
    tails = {
        4: 1,
        6: 1,
    }

    At index = 3, do nothing becos we used up "3"

    At index = 4, add "4" to tails[4] -> tails[5] = 1, tails[4] -= 1
    counter = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 1,
    }
    tails = {
        4: 0
        5: 1,
        6: 1,
    }

    At index = 5, do nothing becos we used up "4"

    At index = 6, add "5" to tails[5] -> tails[6] += 1, tails[5] -= 1
    counter = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
    }
    tails = {
        4: 0
        5: 0,
        6: 2,
    }

    At index = 7, do nothing becos we used up "5"

    We are done!!!

    ref:
    - https://www.youtube.com/watch?v=uJ8BAQ8lASE

    Time    O(N)
    Space   O(N)
    612 ms, faster than 48.64%
"""


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = Counter(nums)
        tails = Counter()
        for x in nums:
            if count[x] == 0:
                continue
            elif tails[x] > 0:
                tails[x] -= 1
                tails[x+1] += 1
            elif count[x+1] > 0 and count[x+2] > 0:
                count[x+1] -= 1
                count[x+2] -= 1
                tails[x+3] += 1
            else:
                return False
            count[x] -= 1
        return True


s = Solution()

a = [1, 2, 3, 3, 4, 5]
print(s.isPossible(a))

a = [1, 2, 3, 3, 4, 4, 5, 5]
print(s.isPossible(a))

a = [1, 2, 3, 4, 4, 5]
print(s.isPossible(a))

a = [1, 2, 3, 3, 4, 4, 5, 5, 6]
print(s.isPossible(a))

a = [1, 2, 3, 4, 4, 5, 6]
print(s.isPossible(a))
