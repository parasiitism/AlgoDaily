"""
    "isomorphic strings" means

    e.g.1
    s1 = aab
    s2 = xxy
    s1 and s2 are isomorphic because a->x, b->y

    e.g.2
    s1 = aab
    s2 = xyx
    s1 and s2 are isomorphic because when a->x, a can not be mapped to y

    e.g.3
    s1 = xyx
    s2 = aab
    s1 and s2 are isomorphic because when a->x, a can not be mapped to y

    Time    O(n)
    Space   O(n)
"""


def isIsomorphic(a, b):
    if len(a) != len(b):
        return False
    # forwad and backward
    ht_f = {}
    ht_b = {}
    for i in range(len(a)):
        c1 = a[i]
        c2 = b[i]
        if c1 in ht_f:
            if ht_f[c1] != c2:
                return False
        if c2 in ht_b:
            if ht_b[c2] != c1:
                return False
        else:
            ht_f[c1] = c2
            ht_b[c2] = c1
    return True


a = "aab"
b = "xxy"
print(isIsomorphic(a, b))

a = "aab"
b = "xyz"
print(isIsomorphic(a, b))

a = "xyz"
b = "aab"
print(isIsomorphic(a, b))

a = "aab"
b = "xxyz"
print(isIsomorphic(a, b))

print("---------------")

"""
    followup:

    Given a list of vocabs, return a list of group of isomorphic strings

    e.g.
    [aab, xxy, xyz, abc, def, xyx]
    return [
        [aab, xxy],
        [xyz, abc, def],
        [xyx]
    ]

    Time    O(n^3)
    Space   O(n)
"""


def groupIsomorphic(strs):
    structures = {}
    structures[strs[0]] = [strs[0]]
    for i in range(1, len(strs)):
        s = strs[i]
        found = False
        for key in structures:
            if isIsomorphic(s, key):
                structures[key].append(s)
                found = True
                break
        if found == False:
            structures[s] = [s]

    res = []
    for key in structures:
        res.append(structures[key])
    return res


a = ['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']
print(groupIsomorphic(a))
