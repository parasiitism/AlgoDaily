
"""
    1st approach:

    Time    
    Space   
"""


def f():
    pass


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(input())  # read a line with a single integer
for t in range(1, T + 1):
    arr = [int(s) for s in input().split(" ")]
    # or a, b = map(int, input().split())
    k = int(input())
    res = f(arr, k)
    print("Case #{}: {}".format(t, res))
    # Or
    print(f"Case #{t}: {res}")
