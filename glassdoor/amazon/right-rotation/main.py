"""
There are 2 strings, s1 and s2, determine if s2 is a rotated version of s1

e.g.1
s1 = "abcde"
s2 = "cdeab"
return true

e.g.2
s1 = "abcde"
s2 = "cbead"
return false
"""


def rightRotate(s1, s2):
    """
        1st approach
        - find s2 in the combined string, s1+s1
        Time    O(n)
        Space   O(n)
    """
    if len(s1) == 0 or len(s2) == 0 or len(s2) > len(s1):
        return False
    com = s1+s1
    return True if com.find(s2) > -1 else False


s1 = "abcde"
s2 = "cdeab"
print(rightRotate(s1, s2))

s1 = "abcde"
s2 = "cbead"
print(rightRotate(s1, s2))
