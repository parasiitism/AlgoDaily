"""
    similar to lc735
    - if positive, just put into stack
    - if negative:
      1. pop the stack if abs(num) is larger than the top positive item in the stack
      2. if the stack becomes empty or top item is negative, pile up the stack with the num
      3. pop the stack if abs(num) == stack[-1], skip appending

    Time    O(n)
    Space   O(n)
    Result 100/100 https://app.codility.com/demo/results/trainingKW42MA-WX8/
"""


def solution(A, B):
    # write your code in Python 3.6
    nums = []
    for i in range(len(A)):
        if B[i] == 0:
            nums.append(-A[i])
        else:
            nums.append(A[i])
    stack = []
    for num in nums:
        if num >= 0:
            stack.append(num)
        else:
            # pop the smaller items from the stack
            while len(stack) > 0 and stack[-1] > 0 and abs(num) > stack[-1]:
                stack.pop()
            # same size asteroid collide
            if len(stack) > 0 and stack[-1] > 0 and abs(num) == stack[-1]:
                stack.pop()
                continue
            # append num to res if empty or stack[-1] < 0
            if len(stack) == 0 or stack[-1] < 0:
                stack.append(num)
    return len(stack)


a = [4, 3, 2, 1, 5]
b = [0, 1, 0, 0, 0]
print(solution(a, b))
