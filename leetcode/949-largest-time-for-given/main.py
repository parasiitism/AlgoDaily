"""
    1st approach: permutation

    Time    O(4!)
    Space   O(4!)
    28 ms, faster than 30.08%
"""


class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        self.times = []
        self.permute(A, "")
        res = None
        for time in self.times:
            hour = time[:2]
            minute = time[2:]
            if int(hour) < 24 and int(minute) < 60:
                if res == None or hour+minute > res:
                    res = hour+minute
        if res == None:
            return ""
        return res[:2] + ':' + res[2:]

    def permute(self, cands, chosen):
        if len(cands) == 0:
            self.times.append(chosen)
        for i in range(len(cands)):
            cand = cands[i]
            self.permute(cands[:i]+cands[i+1:], chosen+str(cand))
