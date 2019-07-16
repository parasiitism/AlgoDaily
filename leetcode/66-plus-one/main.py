"""
    1st approach: carry
    - like add big numbers
    
    16 ms, faster than 93.52%
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if carry > 0:
                temp = digits[i] + carry
                digits[i] = temp % 10
                carry = temp/10
        if carry > 0:
            digits.insert(0, 1)
        return digits


"""
    1st approach: carry
    - like add big numbers
    
    16 ms, faster than 89.69%
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            temp = digits[i] + carry
            num = temp % 10
            carry = temp/10
            res.append(num)
        if carry > 0:
            res.append(carry)
        return res[::-1]
