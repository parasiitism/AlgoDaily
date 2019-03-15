from collections import *

"""
    1st approach:
    - use oredered dict
    - put all the keys into the ordered dict
    - for finding the farthest reach of deletion
    - for each character, decrement the count in the ordereddict
    - check if the occurence in the front of the current char are all zeros

    Time    O(n^2)
    Space   O(n)
    348 ms, faster than 5.04%
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # put all the keys into the ordered dict
        od = OrderedDict()
        for c in S:
            if c in od:
                od[c] += 1
            else:
                od[c] = 1

        res = []
        # for finding the farthest reach of deletion
        farthestReachCountInOd = 0
        deleteCount = 0
        # for each character, decrement the count in the ordereddict
        for c in S:
            od[c] -= 1
            deleteCount += 1
            curIdx = od.keys().index(c)  # idx of current character in ordereddict
            items = od.items()
            farthestReachCountInOd = max(farthestReachCountInOd, curIdx)

            if od[c] == 0:
                isAllZerosFromFront = True
                # in ordereddict,
                # check if the occurence in the front of the current char are all zeros
                for i in range(farthestReachCountInOd, -1, -1):
                    key, cnt = items[i]
                    if cnt > 0:
                        isAllZerosFromFront = False
                        break
                # if yes, do partition
                if isAllZerosFromFront == True:
                    res.append(deleteCount)
                    deleteCount = 0
                    farthestReachCountInOd = 0
                    for i in range(farthestReachCountInOd, -1, -1):
                        key, cnt = items[i]
                        del od[key]
        return res
