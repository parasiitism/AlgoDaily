import collections
""" 
    2nd approach: 2 hashtables
    - 1st hashtable for str1[i] -> str2[i]
    - 2nd hashtable for str2[i] -> str1[i]

    Time  O(n)
    Space O(n)
    24 ms, faster than 99.62%
"""


class Solution(object):
    def isIsomorphic(self, a, b):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        forward = {}
        backward = {}
        for i in range(len(a)):
            c1 = a[i]
            c2 = b[i]
            if c1 not in forward:
                forward[c1] = c2
            else:
                if forward[c1] != c2:
                    return False
            if c2 not in backward:
                backward[c2] = c1
            else:
                if backward[c2] != c1:
                    return False
        return True


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

a = ['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx', 'bbacyba', 'xxyzwxy']
print(groupIsomorphic(a))

print("-----")

"""
    2nd: better approach

    - Compute a word's "signature"

    e.g.
    bbacyba
    0012301

    xxyzwxy
    0012301

    - group the words with the same signature

    so bbacyba and xxyzwxy are groupIsomorphic
    Time    O(nk) k: average number of characters 
    Space   O(n)
"""


def groupIsomorphic(strs):
    def getSignature(word):
        signature = ""
        seen = {}
        nth = 0
        for c in word:
            if c not in seen:
                seen[c] = str(nth)
                nth += 1
            signature += seen[c] + '#'
        return signature

    res = collections.defaultdict(list)
    for s in strs:
        code = getSignature(s)
        res[code].append(s)
    return res.values()


a = ['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']
print(groupIsomorphic(a))

a = ['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx', 'bbacyba', 'xxyzwxy']
print(groupIsomorphic(a))
