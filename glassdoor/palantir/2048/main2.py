"""
    Implement the game 2048 in one dimension
    - Given a array of numbers implement the swipe left function.
        The swipe left function moves the number left and merges equal numbers
    
    e.g.
    - [4,0,2,2] -> [4,0,4,0]
    - [4,2,2,3] -> [8,0,0,3]
    - [8,4,2,2,3] -> [16,0,0,0,3]
    - [0,0,10,-5,-5,0,3] -> 

    https://www.1point3acres.com/bbs/thread-963716-1-1.html
"""


def f(arr):
    n = len(arr)
    stack = []
    for i in range(n):
        x = arr[i]
        if x == 0:
            stack.append((x, i))
        else:
            j = i
            while len(stack) > 0 and stack[-1][0] == x:
                y, j = stack.pop()
                x = x + y
            stack.append((x, j))
    res = n * [0]
    print(stack)
    for x, i in stack:
        res[i] = x
    return res


print(f([4, 0, 2, 2]))
# print(f([4,2,2,3]))
# print(f([8,4,2,2,3]))
# print(f([0,0,10,-5,-5,0,3]))
