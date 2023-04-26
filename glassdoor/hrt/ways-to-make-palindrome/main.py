from collections import *
"""
    Given a string, determine how many ways we could add at most one letter
    to the string so that it is a permutation of a palindrome. 

    e.g. 1
    Input: aabb
    Output: 27

    e.g. 2
    Input: abbb
    Output: 2
"""


def f(S):
    res = 0
    ctr = Counter(S)
    if canFormPalindrome(ctr):
        res += 1
    ascii_of_a = ord('a')
    for i in range(ascii_of_a, ascii_of_a+26):
        c = chr(i)
        ctr[c] += 1
        if canFormPalindrome(ctr):
            res += 1
        ctr[c] -= 1
    return res


def canFormPalindrome(ctr):
    seen_odd = False
    for k in ctr:
        if ctr[k] % 2 == 1:
            if seen_odd:
                return False
            seen_odd = True
    return True


print(f('aabb'))
print(f('abbb'))
