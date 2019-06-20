"""
    add the reversed self until there is no odd digit
"""


def reverseAndAddIfOdd(x):

    numStr = x
    count = 0
    while countOddDigits(numStr) > 0:
        num = int(numStr)
        revNumStr = numStr[::-1]
        revNum = int(revNumStr)

        nextNum = num + revNum
        numStr = str(nextNum)

        count += 1
    return count, numStr


def countOddDigits(s):
    count = 0
    for c in s:
        if int(c) % 2 != 0:
            count += 1
    return count


# # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# # This is all you need for most Code Jam problems.
# # read input to know N
# t = int(input())
# # read N lines
# for i in range(1, t + 1):
#     ri = input()  # raw_input() for python2.7
#     a, b = reverseAndAddIfOdd(ri)
#     print(a, b)

"""
test

4
168
7
2
246
"""

"""
    variation 1:
    add the reversed self until the sum is a palindrome
"""


def reverseAndAddIfNotPalindrome(x):

    numStr = x
    count = 0
    while ifPalindrome(numStr) == False:
        num = int(numStr)
        revNumStr = numStr[::-1]
        revNum = int(revNumStr)

        nextNum = num + revNum
        numStr = str(nextNum)

        count += 1
    return count, numStr


def ifPalindrome(s):
    return s == s[::-1]


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
# read input to know N
t = int(input())
# read N lines
for i in range(1, t + 1):
    ri = input()  # raw_input() for python2.7
    a, b = reverseAndAddIfNotPalindrome(ri)
    print(a, b)

"""
test

3
121
45
26
"""
