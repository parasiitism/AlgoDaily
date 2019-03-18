class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(ops)):
            score = ops[i]
            if len(stack) > 0 and score == 'C':
                pop = stack.pop()
            elif len(stack) > 0 and score == 'D':
                x = stack[-1] * 2
                stack.append(x)
            elif score == '+':
                n = len(stack)
                val = 0
                if n >= 2:
                    val = stack[-2] + stack[-1]
                elif n == 1:
                    val = stack[-1]
                stack.append(val)
            else:
                x = int(score)
                stack.append(x)
        return sum(stack)
