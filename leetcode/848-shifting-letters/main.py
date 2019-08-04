"""
    1st approach: suffix sum + math
    - calculate suffix sums
    - use % to get the index of characters

    e.g.  "abc" and [3,5,9]
    suffixsums =    [17,14,9]
    
    shifting process: 
    a shifts 17 -> r 
    b shifts 14 -> p
    c shifts 9  -> l

    resulf = "rpl"

    TIme    O(n)
    Space   O(n)
    164 ms, faster than 89.77%
"""


class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        suffixSums = len(shifts) * [0]
        suffixSums[-1] = shifts[-1] % 26
        for i in range(len(shifts)-2, -1, -1):
            suffixSums[i] = (suffixSums[i+1] + shifts[i]) % 26
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        res = ''
        for i in range(len(S)):
            c = S[i]
            idx = (suffixSums[i] + ord(c) - 97) % 26
            res += alphabets[idx]
        return res
