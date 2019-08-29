import sys

"""
    1st: sliding window + hashtable
    - count the number of 1s
    - use a fixed sliding window which has least number of zeros to swap

    Time    O(2n)
    Space   O(n)
    816 ms, faster than 7.10%
"""


class Solution(object):
    def minSwaps(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        total = 0
        for x in data:
            total += x
        ht = {0: 0, 1: 0}
        res = sys.maxsize
        for i in range(len(data)):
            ht[data[i]] += 1
            if i >= total:
                lastNum = data[i-total]
                ht[lastNum] -= 1
            if ht[0] + ht[1] == total:
                res = min(res, ht[0])
        return res


"""
    2nd: similar to 1st approach but use a sliding window only

    Time    O(2n)
    Space   O(n)
    756 ms, faster than 31.61%
"""


class Solution(object):
    def minSwaps(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        total = 0
        for x in data:
            total += x
        oneCount = 0
        res = sys.maxsize
        for i in range(len(data)):
            if data[i] == 1:
                oneCount += 1
            if i >= total:
                lastNum = data[i-total]
                if lastNum == 1:
                    oneCount -= 1
            res = min(res, total-oneCount)
        return res
