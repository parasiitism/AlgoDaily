"""
    1st approach: stack
    1. put the numbers into 2 stacks
    2. store the carry and add it to the next digit

    corner cases:
    1. 9 + 1 => 10
    2. "" => "0"

    Time    O(2M+2N)
    Space   O(M+N)
    44 ms, faster than 51.05%
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        stack1 = []
        stack2 = []
        for num in num1:
            stack1.append(int(num))
        for num in num2:
            stack2.append(int(num))
        res = ""
        carry = 0
        while len(stack1) > 0 or len(stack2) > 0:
            val1 = 0
            if len(stack1) > 0:
                val1 = stack1.pop()
            val2 = 0
            if len(stack2) > 0:
                val2 = stack2.pop()
            temp = val1 + val2 + carry
            if temp > 9:
                carry = temp/10
                temp = temp % 10
            else:
                carry = 0
            res = str(temp) + res
        if carry > 0:
            res = '1' + res
        return res


"""
    2nd: 2 pointers

    Time    O(M+N)
    Space   O(M+N)
    36 ms, faster than 54.53%
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ""
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j >= 0:
            a = 0
            if i >= 0:
                a = int(num1[i])
                i -= 1
            b = 0
            if j >= 0:
                b = int(num2[j])
                j -= 1
            temp = a + b + carry
            d = temp % 10
            carry = temp//10
            res = str(d) + res
        if carry > 0:
            res = str(carry) + res
        return res


"""
    3rd: also 2 pointers

    Time    O(M+N)
    Space   O(M+N)
    36 ms, faster than 54.53%
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = []
        i = 0
        j = 0
        carry = 0
        while i < len(num1) or j < len(num2):
            a, b = 0, 0
            if i < len(num1):
                a = int(num1[i])
                i += 1
            if j < len(num2):
                b = int(num2[j])
                j += 1
            d = (a + b + carry) % 10
            carry = (a + b + carry) // 10
            res.append(str(d))
        if carry > 0:
            res.append(str(carry))
        return ''.join(res[::-1])
