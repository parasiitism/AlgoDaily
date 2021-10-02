"""
    Time    O(N)    108 ms
    Space   O(1)    19700 KB
"""


def f():
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end
    n, k = map(int, input().split())  # read a line with 2 integers
    for i in range(k):
        if n % 10 == 0:
            n //= 10
        else:
            n -= 1
    return n


print(f())
