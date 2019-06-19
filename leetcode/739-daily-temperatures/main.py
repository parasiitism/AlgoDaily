"""
    1st approach: stack
    
    Time    O(2n)
    Space   O(n)
    460 ms, faster than 53.26%
"""


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = len(T) * [0]
        stack = []
        for i in range(len(T)):
            t = T[i]
            while len(stack) > 0 and t > stack[-1][0]:
                pop, idx = stack.pop()
                res[idx] = i-idx
            stack.append((t, i))
        return res
