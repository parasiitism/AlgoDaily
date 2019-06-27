"""
questions:
- input only has lowercase letter? yes
- so i need to put them in order? yes, in the original string order
"""


def dedupFromString(s):
    """
    Time    O(n)
    Space   O(n)
    """
    m = {}
    for c in s:
        m[c] = True
    temp = ""
    for c in s:
        if m[c] == True:
            temp += c
            m[c] = False
    return temp


print(dedupFromString("geeksforgeeks"))
print(dedupFromString("characters"))


def dedupFromString(s):
    """
    Time    O(n)
    Space   O(26) -> O(1)

    https://www.geeksforgeeks.org/remove-duplicates-from-a-string-in-o1-extra-space/
    """
    seen = 26*[False]
    temp = ""
    for c in s:
        idx = ord(c)-97
        if seen[idx] == False:
            temp += c
            seen[idx] = True
    return temp


print(dedupFromString("geeksforgeeks"))
print(dedupFromString("characters"))
