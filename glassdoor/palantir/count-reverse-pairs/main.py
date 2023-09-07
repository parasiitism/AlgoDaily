"""
    Given a list of strings, return the number of pairs which the reverse of a string = string.
    The result only count the unique pairs

    e.g.
    ['abc','bac','adc','cba','cba','cda']

    Output: 4

    Explaination
    'abc'->'cba'
    'cba'->'abc'
    'adc'->'cda'
    'cda'->'adc'

    note: there are 2 'cba' which maps to 'abc', but we only count the unique ones
"""


def f1(strs):
    seen = set()
    res = set()
    for s in strs:
        r = s[::-1]
        if s in seen:
            res.add((r, s))
            res.add((s, r))
        else:
            seen.add(r)
    return len(res)


a = ['abc', 'bac', 'adc', 'cba', 'cba', 'cda', 'abc']
print(f1(a))

print("-----")


def f2(strs):
    seen = set()
    counted = set()
    res = 0
    for s in strs:
        r = s[::-1]
        if s in seen:
            if s in counted:
                continue
            counted.add(s)
            res += 2
        else:
            seen.add(r)
    return res


a = ['abc', 'bac', 'adc', 'cba', 'cba', 'cda', 'abc']
print(f2(a))

print("-----")


def f3(strs):
    reverseds = set()
    for s in strs:
        r = s[::-1]
        reverseds.add(r)
    res = set()
    for s in strs:
        if s in reverseds:
            res.add(s)
    return len(res)


a = ['abc', 'bac', 'adc', 'cba', 'cba', 'cda', 'abc']
print(f3(a))
