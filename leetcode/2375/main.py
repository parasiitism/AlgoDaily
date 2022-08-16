"""
    greedy

    Time    O(N)
    Space   O(N)
    35 ms, faster than 75.00%
"""


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res, stack = [], []
        pattern += 'I'
        for i in range(len(pattern)):
            c = pattern[i]

            # append the small number in the stack
            num = str(i + 1)
            stack.append(num)

            # add the reverse of the stack to the res
            if c == 'I':
                res += stack[::-1]
                stack = []
        return ''.join(res)
