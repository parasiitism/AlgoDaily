"""
    1st approach: math

    importent case: negative numbers

    here is how a computer stores negative numbers using Two's complement method
    - first bit = sign
    - rest of the bits = number
    
    e.g. 2^3 signed numbers
    0   000
    1   001
    2   010
    3   011
    -4  100
    -3  101
    -2  110
    -1  111

    we see that
    -4 = 4 = 100
    -3 = 5 = 101
    -2 = 6 = 110
    -1 = 7 = 111
    negative number + 2^3 = positive number = binary represenation of what we want

    ref:
    - https://en.wikipedia.org/wiki/Two%27s_complement
    
    Time    O(n)
    Space   O(n)
    20 ms, faster than 65.74%
"""


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        if num < 0:
            num += 2**32
        m = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f'
        }
        arr = []
        while num > 0:
            temp = ""
            if num % 16 > 9:
                temp = m[num % 16]
            else:
                temp = str(num % 16)
            arr.append(temp)
            num /= 16
        return ''.join(arr[::-1])


s = Solution()
print(s.toHex(1234))
print(s.toHex(2516))
print(s.toHex(-1))
print(s.toHex(-10))
print("-----")

"""
    followup: compare 2 hexadecimal numbers

    e.g. 4d2(1234) vs 9d4(2516)
"""


def compare(A, B):
    if len(A) > len(B):
        return A
    elif len(B) > len(B):
        return B
    A = A.lower()
    B = B.lower()
    for i in range(len(A)):
        a = ord(A[i])
        b = ord(B[i])
        if a > b:
            return A
        elif b > a:
            return B
    return ""


print(compare("a", "1"))
print(compare("f", "11"))
print(compare("4d2", "9d4"))
print(compare("9d3", "9d4"))
print(compare("9d5", "9d4"))
