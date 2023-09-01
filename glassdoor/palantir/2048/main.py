"""
    Implement the game 2048 in one dimension
    - Given a array of numbers implement the swipe left function.
        The swipe left function moves the number left and merges equal numbers
    
    e.g.
    - [4,0,2,2] -> [4,4,0,0]
    - [4,2,2,3] -> [4,4,0,3]
    - [8,4,2,2,3] -> [8,4,4,3,0]
    - [0,0,10,-5,-5,0,3] -> [10, -10, 3, 0, 0, 0, 0]

    https://www.1point3acres.com/bbs/thread-963716-1-1.html
"""


def f(arr):
    n = len(arr)
    stack = []
    for i in range(n):
        x = arr[i]
        if x == 0:
            continue
        if len(stack) > 0 and stack[-1] == x:
            stack[-1] += x
        else:
            stack.append(x)
    res = n * [0]
    for i in range(len(stack)):
        res[i] = stack[i]
    return res


print(f([4, 0, 2, 2]))
print(f([4, 2, 2, 3]))
print(f([8, 4, 2, 2, 3]))
print(f([0, 0, 10, -5, -5, 0, 3]))
