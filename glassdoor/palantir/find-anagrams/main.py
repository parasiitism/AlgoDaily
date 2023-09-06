"""
    Given a string and a dictionary (list of strings), 
    return all anagrams of the string that are also in the dictionary

    eg: "race", ["bat", "acer", "caer", "apple"] => return ["acer","caer"]
"""


def find_anagrams(A, target):
    ctr_target = genKey(target)
    res = []
    for s in A:
        key = genKey(s)
        if key == ctr_target:
            res.append(s)
    return res


def genKey(s):
    ctr = 26 * [0]
    for c in s:
        i = ord(c) - ord('a')
        ctr[i] += 1
    return tuple(ctr)


a = ["bat", "acer", "caer", "apple"]
b = 'race'
print(find_anagrams(a, b))
