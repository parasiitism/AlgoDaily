from collections import *

"""
    Time    O(N)
    Space   O(N)
"""


def f():
    n = input()
    s = input()
    cnter = Counter()
    for c in s:
        cnter[c] += 1
    if cnter['A'] > cnter['D']:
        print('Anton')
    elif cnter['A'] < cnter['D']:
        print('Danik')
    else:
        print('Friendship')


f()
