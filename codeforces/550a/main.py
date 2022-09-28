"""
    - check if substring "AB" goes before "BA", 
    - if no, then check if "BA" goes before "AB"

    Time    O(N)
    Space   O(1)
"""


def f():
    s = input()
    b0 = solve(s, 'AB')
    if b0 == True:
        print('YES')
        return
    b1 = solve(s, 'BA')
    if b1 == True:
        print('YES')
        return
    print('NO')


def solve(s, target):
    rev_target = target[::-1]
    n = len(s)
    first_target_idxs = None
    for i in range(n-1):
        sub = s[i] + s[i+1]
        if sub == target:
            first_target_idxs = [i, i+1]
            break
    first_rev_target_idxs = None
    for i in range(n-2, -1, -1):
        sub = s[i] + s[i+1]
        if sub == rev_target:
            first_rev_target_idxs = [i, i+1]
            break
    if first_target_idxs == None or first_rev_target_idxs == None:
        return False
    indices = set(first_target_idxs + first_rev_target_idxs)
    if len(indices) != 4:
        return False
    return True


f()
