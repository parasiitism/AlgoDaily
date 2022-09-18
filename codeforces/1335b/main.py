"""
    greedy
    - First contruct a substring which contains 'b' distinct characters
    - Second duplicate that substring to make a string of length 'n'

    Time    O(N) 171 ms	
    Space   O(N) 5900 KB
"""


def f():
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    T = int(input())
    for _ in range(T):
        n, a, b = [int(c) for c in input().split()]
        distincts = alphabets[:b]
        window = distincts + (a - len(distincts)) * distincts[-1]
        d = n // a
        r = n % a
        res = d * window + window[:r]
        print(res)


f()
