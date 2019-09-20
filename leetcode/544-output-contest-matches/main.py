import math
import json

"""
    1st: math + json serialization
    - i am not sure if it cheats cos i use json serialization
    
    e.g. 16
    1. we form [1, 16, 8, 9, 4, 13, 5, 12, 2, 15, 7, 10, 3, 14, 6, 11] by doing math
    2. then we form [[[[1, 16], [8, 9]], [[4, 13], [5, 12]]], [[[2, 15], [7, 10]], [[3, 14], [6, 11]]]] iteratively
    3. we use json.dumps to serialize the array

    Time    2 * O(nlogn) + O(N)
    Space   O(n)
    16 ms, faster than 87.34%
"""


class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        sq = self.getSequence(n)
        # O(NlogN) because we basically need to all the nodes O(logN) times
        while len(sq) > 2:
            temp = []
            for i in range(0, len(sq), 2):
                popA = sq[i]
                popB = sq[i+1]
                temp.append([popA, popB])
            sq = temp
        # O(N)
        return json.dumps(sq).replace('[', '(').replace(']', ')')

    def getSequence(self, n):
        # O(NlogN) because we basically need to all the nodes O(logN) times
        data = [1, 2]
        for i in range(2, int(math.log(n)/math.log(2)) + 1):
            temp = []
            target = 2**i + 1
            for x in data:
                temp.append(x)
                temp.append(target - x)
            data = temp
        return data
