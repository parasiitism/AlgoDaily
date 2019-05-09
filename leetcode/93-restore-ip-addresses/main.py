"""
    1st approach: combinations
    - the basic idea is the slice the candidates with 1 digit, 2 digits and 3 digits
    - remember to check if the slice is within a legit range
        e.g. "23" is legit because 10 <= 23 <= 99
        e.g. "001" is not legit because i is not 100 <= x <= 255

    Time    O(3^n)
    Space   O(3^n)
    24 ms, faster than 92.86% 
"""

class Solution(object):
    def __init__(self):
        self.res = []

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]

        24 ms, faster than 92.86% 
        """
        self.helper(s, [])
        return self.res
    
    def helper(self, cands, chosen):
        if len(cands) == 0 and len(chosen) == 4:
            ip = '.'.join(chosen)
            self.res.append(ip)
        if len(chosen) > 4:
            return
        if len(cands) > 0:
            a = cands[0]
            remain = cands[1:]
            self.helper(remain, chosen+[a])
        if len(cands) > 1:
            a = cands[:2]
            if int(a) >= 10 and int(a) <= 99:
                remain = cands[2:]
                self.helper(remain, chosen+[a])
        if len(cands) > 2:
            a = cands[:3]
            if int(a) >= 100 and int(a) <= 255:
                remain = cands[3:]
                self.helper(remain, chosen+[a])

a = "25525511135"
print(Solution().restoreIpAddresses(a))

a = "0000"
print(Solution().restoreIpAddresses(a))

a = "00000"
print(Solution().restoreIpAddresses(a))

a = "01010"
print(Solution().restoreIpAddresses(a))

a = "12345432"
print(Solution().restoreIpAddresses(a))