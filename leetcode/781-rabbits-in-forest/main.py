import math

"""
    1st approach: hastable + math
    - very tricky question

    e.g. [0,0,1,1,1]
    - the first two 0 are unique rabbits
    - the [1,1,1] should actually be regarded as [1,1] and [1] because the first two 1 should fall into the same group,
        and the last 1 should be in another group
    
    lets consider another case [0,0,1,1,1,1,1,1,1,2,2,2,2,2]
    - [0,0] are unique
    - [1,1,1,1,1,1,1] should be regarded as [1,1] [1,1] [1,1] [1]
    - [2,2,2,2,2] should be regarded as [2,2,2] [2,2]
    - then we can do math to calculate
        - for 0, there 2
        - for 1, groupCount * rabbitCount = ceil(7/(1+1)) * (1+1) = ceil(7/2) * 2 = 8
        - for 2, groupCount * rabbitCount = ceil(5/(2+1)) * (2+1) = ceil(5/3) * 3 = 6
    - total = 16

    Time    O(n)
    Space   O(n)
    28 ms, faster than 65.50%
"""


class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        m = {}
        for ans in answers:
            if ans not in m:
                m[ans] = 1
            else:
                m[ans] += 1
        res = 0
        for key in m:
            if key == 0:
                res += m[key]
            else:
                if m[key] > key + 1:
                    groupCount = math.ceil(m[key]/(key+1.0))
                    res += int(groupCount) * (key + 1)
                else:
                    res += key + 1
        return res
