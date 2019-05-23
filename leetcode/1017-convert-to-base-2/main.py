"""
    classic approach: negabinary conversion

    ref:
    - https://en.wikipedia.org/wiki/Negative_base
    - https://www.geeksforgeeks.org/convert-number-negative-base-representation/

    13/-2 = -6 mod 1
    -6/-2 =  3 mod 0
    3/-2  = -1 mod 1
    -1/-2 =  1 mod 1
    1/-2  =  0 mod 1

    Time    O(logn)
    Space   O(1)
    12 ms, faster than 99.84%
"""


class Solution(object):

    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        if N == 0:
            return "0"
        res = ""
        while N != 0:
            reminder = N % -2
            N /= -2
            # cautions: we just want positive reminder
            # e.g.
            #   146/-3 = -49, 146%-3 = -1 because -49(-3)-1 = 146
            # BUT what we want is
            #   146/-3 = -48, 146%-3 = 2 because -48(-3)+2 = 146
            if reminder < 0:
                reminder += 2
                N += 1
            res = str(reminder) + res
        return res

    def baseNeg2ToNum(self, s):
        """
            followup1: convert negabinary back to a number
        """
        res = 0
        for i in range(len(s)-1, -1, -1):
            idx = len(s) - 1 - i
            temp = int(s[i]) * ((-2)**idx)
            res += temp
        return res

    def neg2Addition(self, A, B):
        """
            followup2: add 2 negabinary numbers(present from the front)

            ref:
            - https://en.wikipedia.org/wiki/Negative_base#Addition

            Carry:          1 −1  0 −1  1 −1  0  0  0
            First addend:         1  0  1  0  1  0  1
            Second addend:        1  1  1  0  1  0  0 + addition
                            --------------------------
            Number:         1 −1  2  0  3 −1  2  0  1 when we come with a number, lookup from the hashtable
            -----------------------------------------
            Bit (result):   1  1  0  0  1  1  0  0  1
            Carry:          0  1 −1  0 −1  1 −1  0  0 <- each number will be moved to the carry on the top in the next bit
        """
        lookup = {
            -2: (0, 1),
            -1: (1, 1),
            0: (0, 0),
            1: (1, 0),
            2: (0, -1),
            3: (1, -1),
        }
        carry = 0
        result = []
        # do addition
        while len(A) > 0 or len(B) > 0:
            a = 0
            if len(A) > 0:
                a = A.pop()
            b = 0
            if len(B) > 0:
                b = B.pop()
            temp = a + b + carry
            res, carry = lookup[temp]
            result.append(res)
        # if there is still a carry
        while carry != 0:
            res, carry = lookup[carry]
            result.append(res)
        # remove leading zeros
        while result[-1] == 0:
            result.pop()
        return result[::-1]

    def neg2AdditionFromEnd(self, A, B):
        """
            followup2: add 2 negabinary numbers(present from the END)
        """
        lookup = {
            -2: (0, 1),
            -1: (1, 1),
            0: (0, 0),
            1: (1, 0),
            2: (0, -1),
            3: (1, -1),
        }
        carry = 0
        result = []
        # do addition
        while len(A) > 0 or len(B) > 0:
            a = 0
            if len(A) > 0:
                a = A.pop(0)
            b = 0
            if len(B) > 0:
                b = B.pop(0)
            temp = a + b + carry
            res, carry = lookup[temp]
            result.append(res)
        # if there is still a carry
        while carry != 0:
            res, carry = lookup[carry]
            result.append(res)
        # remove leading zeros
        while result[-1] == 0:
            result.pop()
        return result


# test int to neg2
print(Solution().baseNeg2(13))
print(Solution().baseNeg2(134))
print("-----")

# test neg2 to int
print(Solution().baseNeg2ToNum("11101"))
print(Solution().baseNeg2ToNum("110011010"))
print("-----")

# test neg2Addition naive
x = Solution().baseNeg2ToNum("1011") + Solution().baseNeg2ToNum("0110")
y = Solution().baseNeg2(x)
print(x, y)
print("-----")

# test neg2Addition(present from the front)
print(Solution().neg2Addition(
    [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 0]))
print(Solution().neg2Addition([1, 0, 1, 1], [0, 1, 1, 0]))

print("-----")

# test neg2Addition(present from the end)
print(Solution().neg2AdditionFromEnd(
    [1, 0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 1, 1]))
print(Solution().neg2AdditionFromEnd([1, 1, 0, 1], [0, 1, 1, 0]))
