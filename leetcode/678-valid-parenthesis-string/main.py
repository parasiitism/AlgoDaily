"""
    1st approach: recursion

    Time    O(3^n)
    Space   O(n)
    LTE
"""
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        # stack = [(s, 0, 0)]
        return self.helper(s, 0, 0)
        
    def helper(self, cands, openCnt, closeCnt):
        if len(cands) == 0:
            if openCnt == closeCnt:
                return True
            return False
        b = False
        first = cands[0]
        if first == ' ':
            b = b or self.helper(cands[1:], openCnt, closeCnt)
        elif first == '(':
            b = b or self.helper(cands[1:], openCnt+1, closeCnt)
        elif first == ')':
            if openCnt > closeCnt:
                b = b or self.helper(cands[1:], openCnt, closeCnt+1)
        elif first == '*':
            b = b or self.helper(cands[1:], openCnt, closeCnt)
            b = b or self.helper(cands[1:], openCnt+1, closeCnt)
            if openCnt > closeCnt:
                b = b or self.helper(cands[1:], openCnt, closeCnt+1)
        return b

"""
    2nd learned from others:

    ref:
    - https://leetcode.com/problems/valid-parenthesis-string/discuss/107570/JavaC%2B%2BPython-One-Pass-Count-the-Open-Parenthesis
    - https://www.cnblogs.com/grandyang/p/7617017.html

    Time    O(n)
    Space   O(1)
    20 ms, faster than 79.33%
"""
class Solution(object):
    def checkValidString(self, s):
        # max number of ( and min numb of (
        
        # minOpenCnt considers each '*' as ')' as MUCH as possible
        minOpenCnt = 0
        # maxOpenCnt considers each '*' as '(', which should never be negative
        maxOpenCnt = 0
        for c in s:
            if c == '(':
                maxOpenCnt += 1
                minOpenCnt += 1
            if c == ')':
                maxOpenCnt -= 1
                # if there is enough min open, (, we decrement it
                if minOpenCnt > 0:
                    minOpenCnt -= minOpenCnt
            if c == '*':
                maxOpenCnt += 1
                # if there is enough min open, (, we decrement it
                if minOpenCnt > 0:
                    minOpenCnt -= minOpenCnt
            # if we consider all * as ( and we still dont have enough ), return False
            if maxOpenCnt < 0:
                return False
        return minOpenCnt == 0

print(Solution().checkValidString("(*))"))