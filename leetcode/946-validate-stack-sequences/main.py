"""
    1st: stack
    
    Time    O(M+N)
    Space   O(M)
    60 ms, faster than 44.22%
"""


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        for x in pushed:
            stack.append(x)
            while len(stack) > 0 and len(popped) > 0 and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        return len(stack) == 0 and len(popped) == 0
