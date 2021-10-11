
"""
    Time    O(N)    154 ms
    Space   O(1)    6568 KB
"""


def f():
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end
    x = int(input())  # read a line with 2 integers
    if x <= 2:
        print('NO')
    else:
        if x % 2 == 0:
            print('YES')
        else:
            print('NO')


f()
