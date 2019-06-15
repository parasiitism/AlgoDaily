"""
    its also a facebook hackercup question
    https://gist.github.com/mstepniowski/4660602
"""


def maxBeauty(s):
    ht = {}
    s = s.lower()
    for c in s:
        if c not in ht:
            ht[c] = 1
        else:
            ht[c] += 1
    occurences = []
    for key in ht:
        occurences.append((ht[key], key))
    occurences = sorted(occurences, key=lambda x: -x[0])
    res = 0
    n = 26
    while len(occurences) > 0:
        occur, key = occurences.pop(0)
        res += occur * n
        n -= 1
    return res


print(maxBeauty('a'))
print(maxBeauty('ab'))
print(maxBeauty('abc'))
print(maxBeauty('aba'))
print(maxBeauty('abac'))
print(maxBeauty('abcc'))

print("-----")

n = int(input())
# read N lines
for i in range(n):
    s = input()  # raw_input() for python2.7
    result = maxBeauty(s)
    print(result)

"""
a
ab
abc
aba
abac
abcc
calvin
"""
