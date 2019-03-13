"""
    questions to ask:
    - any malformed expression? no
    - any other characters? only digit and +-*/ and space
"""

"""
    1st approach:
    - use 1 queue
    - for every number or + / -, put it into the queue
    - but for * and /, multiply or divide the next item with the last item in the queue

    Time    O(2n)
    Space   O(n) the queue
    4152 ms, faster than 5.09%
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        queue = []
        i = 0
        shouldMultiply = False
        shouldDivide = False
        while i < len(s):
            if s[i].isdigit():
                temp = int(s[i])
                j = i+1
                while j < len(s) and s[j].isdigit():
                    temp = temp*10 + int(s[j])
                    j += 1
                if shouldMultiply:
                    queue[-1] = temp * queue[-1]
                    shouldMultiply = False
                elif shouldDivide:
                    queue[-1] = queue[-1] / temp
                    shouldDivide = False
                else:
                    queue.append(temp)
                i = j
            else:
                if s[i] == "*":
                    shouldMultiply = True
                elif s[i] == "/":
                    shouldDivide = True
                elif s[i] == "+" or s[i] == "-":
                    queue.append(s[i])
                i += 1
        shouldAdd = False
        shouldMinus = False
        result = 0
        while len(queue) > 0:
            pop = queue.pop(0)
            if isinstance(pop, int):
                if shouldAdd:
                    result += pop
                    shouldAdd = False
                elif shouldMinus:
                    result -= pop
                    shouldMinus = False
                else:
                    result += pop
            elif pop == "+":
                shouldAdd = True
            elif pop == "-":
                shouldMinus = True
        return result


# string = '0'
# print(string.isdigit())

# a = "da"
# print(isinstance(a, int))

# a = 5
# print(isinstance(a, int))

# 47
print(Solution().calculate("3+22*2"))
# 1
print(Solution().calculate(" 3/2 "))
# 5
print(Solution().calculate(" 3+5 / 2"))
# 7
print(Solution().calculate("3+5/2*2"))
# 6
print(Solution().calculate("1+2 *5/3+6/4*2 "))
# 45
print(Solution().calculate("100-1-2-3-4-5-6-7-8-9-10"))
# -5
print(Solution().calculate("0-5"))
# -2147483647
print(Solution().calculate("0-2147483647"))
