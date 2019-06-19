"""
    Have to visit all distinct destinations in array a in the shortest possible interval of consecutive days
    where days are indices in the array

    note:
    - if there are more than one result, return any one of them 

    Rephrase: shortest substring with all characters

    Time    O(n)
    Space   O(n)
"""


def f(s):
    m = {}
    for i in range(len(s)):
        c = s[i]
        if c not in m:
            m[c] = 1
        else:
            m[c] += 1
    numberOfKeys = len(m)
    slow = 0
    res = s
    m = {}
    for i in range(len(s)):
        c = s[i]
        if c not in m:
            m[c] = 1
        else:
            m[c] += 1
        while len(m) == numberOfKeys:

            if i-slow+1 < len(res):
                res = s[slow:i+1]

            last = s[slow]
            m[last] -= 1
            if m[last] == 0:
                del m[last]
            slow += 1
    return res


a = "ababcdefcd"
print(f(a))

a = "baaaabb"
print(f(a))

a = "baaaabc"
print(f(a))
