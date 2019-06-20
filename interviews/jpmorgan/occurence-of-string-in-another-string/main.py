"""
    Find the number of occurence of string T in string S

    ref:
    - https://www.1point3acres.com/bbs/thread-282628-1-1.html
"""


def f(S, T):
    if len(S) < len(T):
        return 0
    count = 0
    for i in range(len(S)-len(T)+1):
        sub = S[i:i+len(T)]
        if sub == T:
            count += 1
    return count


print(f('abc', 'abc'))
print(f('abcabcabcabc', 'abc'))
print(f('abcabcabcabc', 'abcabc'))
